import lexicon
from ccg_algorithm import ccg_algorithm


def test_lex_1():
    assert ccg_algorithm(
        lex=lexicon.LEX1,
        const=lexicon.CONST1,
        max_deg=lexicon.MAX_DEG1,
        sentence='w1 w2 w3 w4 w5 w6 w7 w8'
    )


def test_lex_2():
    assert ccg_algorithm(
        lex=lexicon.LEX2,
        const=lexicon.CONST2,
        max_deg=lexicon.MAX_DEG2,
        sentence='w1 w2 w3 w4 w5 w6 w7 w8 w9 w10 w11 w12 w13'
    )
