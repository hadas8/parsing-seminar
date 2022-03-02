# Polynomial Time Parsing Algorithm for CCG

A Python implemantation of a polynomial-runtime algorithm for parsing CCG grammars, developed by Kulmann and Sata (2014).

## Description

The attached Python implemntation for the polynomial-runtime algorithm developed by Kuhlmann and Sata (2014), demonstrates the algorithm's ability to parse sentences in mildly context-sensitive grammar with CCG formalisms: application and compositions of singular and multiple degrees. This is done in a polynomial runtime complexity, with respect to the length of the input string.

The script demonstrates the examples above, and can be further enhanced to include additional rules for supporting more advanced features of mildly-context sensitive languages, such as type-raising. New lexicon examples can be added and examined to allow parsing of different sentences in English and in other languages.

For addiditonal information about CCG grammars and the algorithm, A PDF file describing my project is attached, along with the references and source material.

## Implementation Details

The script is submitted in three Python files:
-	ccg_algorithm.py – The main module which calls the algorithm. This is the execution file and it demonstrates the parsing of the strings in the examples above.
-	Rules.py – The main algorithm implementation.
-	Lexicon.py – Example lexicons for the script.

 
