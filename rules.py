import re


class Rules(object):
    """
    stores rules and logic for parsing a sentence in CCG
    """

    def __init__(self, constant, max_deg):
        self.constant = constant
        self.max_deg = max_deg
        self.sentence = None

    def arity(self, cat):
        """
        calculates the arity (number of slashes) in a category
        """
        length = len(cat)
        if re.search(r'[/\\]', cat[0]):
            return length
        else:
            return length - 1

    def direction(self, cat):
        """
        calculates direction of rule to be implemented
        """
        if cat[0][0] == '/':
            return 'forward'
        elif cat[0][0] == '\\':
            return 'backward'

    def match_categoreis(self, cat1, cat2):
        r"""
        return True for matching categories : A, \A or A/, A
        """
        cat1[0] = cat1[0][1:]
        return cat1 == cat2

    def parse(self, parse_sentence, i):
        """
        receives a sentence already divided into lexical categories and index i,
        activate rule1 for the category i
        """
        self.sentence = parse_sentence
        main_cat = self.sentence[i]
        return self.rule1(main_cat, i, i + 1)

    def parse_new_cat(self, category, deg, i, j):
        """
        a helper function for rules 1,4,5
        receives a category, and degree of split
        parses the next step
        """
        # we split X|Y: part 1 = X, part 2 = |Y
        part1 = category[:-deg]
        part2 = category[-deg:]
        slash_dir = self.direction(part2)

        # check the direction of the slash before Y
        if slash_dir == 'forward' and j != len(self.sentence):
            sec_cat = self.sentence[j]
            j = j + 1
        elif slash_dir == 'backward' and i != 0:
            sec_cat = self.sentence[i - 1]
            i = i - 1
        else:
            return

        # split the second category Y|Z: part 3 = Y, part 4 = |Z
        length = len(part2)
        part3 = sec_cat[:length]
        part4 = sec_cat[length:]

        # if we found a match Y, we combine: X|Z
        if self.match_categoreis(part2, part3):
            new_cat = part1 + part4
            return new_cat, part1, part4, i, j

    def rule1(self, category, i, j):
        r"""
        apply rule 1 to the category:
        X/Y Y|Z -> X|Z
        Y|Z X\Y -> X|Z
        X,Y,Z are (possibly empty) stacks of m arguments(atomic categories divided by slashes in both directions): |X_m|X_m-1|...|X_1 
        | can be \ or /
        """
        ar = self.arity(category)

        # if there are no slashes, the category is atomic,
        # if we have reached the atomic category 'S' covering the whole sentence, we have succeeded
        if ar == 0:
            if category == ['S'] and i == 0 and j == len(self.sentence):
                return True
            return

        # for each degree of arity, we will attempt to split the category and match it with the adjacent word
        for deg in range(min(ar, self.max_deg), 0, -1):
            result = self.parse_new_cat(category, deg, i, j)
            if result:
                new_cat, part1, part4, i, j = result

                # if the arity is too big, we activate rule 2 instead
                if self.arity(new_cat) > self.constant:
                    return self.rule2(part1, part4, i, j)

                # if the arity is small enough, we continue with the new category
                else:
                    return self.rule1(new_cat, i, j)

    def rule2(self, part1, part4, i, j):
        """
        if the arity is too big on the product of rule 1, we apply rule 2 instead
        this is an intermediate step between X|Y Y|Z and X|Z
        We are splitting Y|Z in order to work with smaller arities
        """
        ar = self.arity(part1)
        max_ar = self.constant - ar

        # while the arity is too big, we apply rule
        # once the arity is small enough, we apply rule 3
        # and return to the complete category from rule 1
        while self.arity(part4) > max_ar:
            result = self.rule4(part4, i, j, max_ar)
            if result:
                part4, i, j = result
            else:
                return
        return self.rule3(part1, part4, i, j)

    def rule3(self, part1, part4, i, j):
        """
        Once the arity is small enough,
        return the new category to be parsed by rule 1
        """
        new_cat = part1 + part4
        return self.rule1(new_cat, i, j)

    def rule4(self, split_cat, i, j, max_ar):
        r"""
        This rule is parallel to rule 1,
        but takes only a split category rather than the whole category
        we continue the smae way as rule 1:
        X/Y Y|Z -> X|Z
        Y|Z X\Y -> X|Z
        this time X|Y is the split category (part4 of rule 1)
        and Y|Z is the next category
        """
        ar = self.arity(split_cat)

        # when the is still too big,
        # we will aply this rule to combine with the next category
        # the same way as in rule 1 
        for deg in range(min(ar, self.max_deg), 0, -1):
            result = self.parse_new_cat(split_cat, deg, i, j)
            if result:
                new_cat, part1, part4, i, j = result

                # if the arity of the new category is bigger than the constant
                # we must split it again, we call rule 5 for that
                if self.arity(new_cat) > self.constant:
                    max_ar = self.constant - self.arity(part1)
                    return self.rule5(part1, part4, i, j, max_ar)
                else:
                    return new_cat, i, j

    def rule5(self, old_part1, part4, i, j, max_ar):
        """
        rule 5 is the deepest part of the recursion
        it keeps parsing the the split category
        as long as the arity is too big
        when the arity is finally small enough, we call rule 6
        rule 6 returns from the recursion
        and combine with the first part of the category (from rule 4)  
        """
        ar = self.arity(part4)
        if ar <= max_ar:
            return self.rule6(old_part1, part4, i, j)
        else:
            for deg in range(min(ar, self.max_deg), 0, -1):
                result = self.parse_new_cat(part4, deg, i, j)
                if result:
                    new_cat, part1, part4, i, j = result
                    if self.arity(new_cat) > self.constant:
                        max_ar = self.constant - self.arity(part1)
                    return self.rule5(old_part1, new_cat, i, j, max_ar)

    def rule6(self, part1, part4, i, j):
        """
        parallel to rule 3, but with a product of a split category
        the rule combines back the split category from rule 4 
        to continue parsing in rule 2
        """
        new_cat = part1 + part4
        return new_cat, i, j
