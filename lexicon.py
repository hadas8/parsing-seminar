"""
lexicon example from Kuhlmann and Sata
"""
LEX1 = {
   'w1' : r'A',
   'w2' : r'B',
   'w3' : r'C\A/F',
   'w4' : r'S/E',
   'w5' : r'E/H\C',
   'w6' : r'F/G\B',
   'w7' : r'G',
   'w8' : r'H'
}
CONST1 = 3
MAX_DEG1 = 1

"""
lexicon example that covers all the rules
"""
LEX2 = {
   'w1' : r'A',
   'w2' : r'H',
   'w3' : r'J',
   'w4' : r'D/E',
   'w5' : r'S\A/B',
   'w6' : r'B/C\D',
   'w7' : r'E/F/G',
   'w8' : r'G\H/I',
   'w9' : r'I\J/K',
   'w10' : r'K/L',
   'w11' : r'L',
   'w12' : r'F',
   'w13' : r'C'
}
CONST2 = 3
MAX_DEG2 = 1

"""
Another example from Kuhlmann and Sata,
derivations with higher degree
"""
LEX3 = {
   'Louise' : r'N',
   'might' : r'S\N/S\N',
   'marry' : r'S\N/N',
   'Harry' : r'N'
} 
CONST3 = 5
MAX_DEG3 = 2