"""
ccg_algorithm is a boolean algorithm that receive a lexicon and a sentence
and returns true if the sentence may be parsed with the lexicon
if not, returns false.
"""

import re
import lexicon
import rules


def ccg_algorithm(lex, const, max_deg, sentence):
    split_sentence = sentence.split()
    parse_sentence = []
    sentence_rules = rules.Rules(const, max_deg)

    # switching each word with it's lexicon category
    # each category is represented as a list of strings, 
    # for example: X/Y\Z -> ['X', '/Y', '\Z']
    for word in split_sentence:
        cat = lex.get(word)
        parse_sentence.append(re.findall(r'[/\\]?.', cat))

    # we search the sentence for a category that starts with 'S'
    # this is where we begin to parse
    # if the parsing of the sentence was successful, return True
    for i, word in enumerate(parse_sentence):
        if word[0] == 'S':
            return sentence_rules.parse(parse_sentence, i)
    return False        


if __name__ == "__main__":
    print("First example: ")
    sentence1 = 'w1 w2 w3 w4 w5 w6 w7 w8'
    result = ccg_algorithm(
        lex = lexicon.LEX1,
        const = lexicon.CONST1,
        max_deg = lexicon.MAX_DEG1,
        sentence = sentence1
    )
    print("Sentence to parse: " + sentence1)
    if result:
        print("The sentence was parsed successfully!")
    else:
        print("The sentence cannot be parsed with the given lexicon.")

    print()
    print("Second example: ")
    sentence2 = 'w1 w2 w3 w4 w5 w6 w7 w8 w9 w10 w11 w12 w13'
    result = ccg_algorithm(
        lex = lexicon.LEX2,
        const = lexicon.CONST2,
        max_deg = lexicon.MAX_DEG2,
        sentence = sentence2
    )
    print("Sentence to parse: " + sentence2)
    if result:
        print("The sentence was parsed successfully!")
    else:
        print("The sentence cannot be parsed with the given lexicon.")


    print()
    print("Third example: ")
    sentence3a = 'Louise might marry Harry'
    sentence3b = 'Louise marry Harry'
    sentence3c = 'Louise might Harry'
    result = ccg_algorithm(
        lex = lexicon.LEX3,
        const = lexicon.CONST3,
        max_deg = lexicon.MAX_DEG3,
        sentence = sentence3a
    )
    print("Sentence to parse: " + sentence3a)
    if result:
        print("The sentence was parsed successfully!")
    else:
        print("The sentence cannot be parsed with the given lexicon.")
    result = ccg_algorithm(
        lex = lexicon.LEX3,
        const = lexicon.CONST3,
        max_deg = lexicon.MAX_DEG3,
        sentence = sentence3b
    )
    print("Sentence to parse: " + sentence3b)
    if result:
        print("The sentence was parsed successfully!")
    else:
        print("The sentence cannot be parsed with the given lexicon.")
    result = ccg_algorithm(
        lex = lexicon.LEX3,
        const = lexicon.CONST3,
        max_deg = lexicon.MAX_DEG3,
        sentence = sentence3c
    )
    print("Sentence to parse: " + sentence3c)
    if result:
        print("The sentence was parsed successfully!")
    else:
        print("The sentence cannot be parsed with the given lexicon.")
