# Machine Assignment 1
# 1 Convert Decimal Mantissa to Binary Mantissa
Write a program that receives a real number in decimal (base 10) and converts it into binary (base 2).
<br />   • You must implement the algorithm discussed in Chapter 1.
<br />   • You may not use libraries or built-in functions (e.g., Double.toHexString(. . . ) in Java or ”{0:b}”.format(. . . ) in Python)
<br />You may assume that all input is well-formed (i.e., all inputs are valid real numbers). You need not (and should not) expect illegal inputs (e.g., ”0.1LOL”).
# 1.1 Legal Input
Ideally, your program should handle all real numbers including: negative numbers, positive numbers, and those with non-zero integer components. However, you may (without penalty) restrict your expected input to numbers in the domain 0 to (inclusive) to 1 (exclusive)–i.e., x ∈ [0, 1).
# 1.2 Sample Execution & Output
All input must be handled through command line arguments. Suppose you were implementing your solution in a Python 3.7 program, convert dec to bin.py. Program execution should be similar to:
<br />./convert_dec_to_bin.py 0.5 0.25 0.75
<br />The output should take a form similar to:
<br />| Base 10 | Base 2 |
<br />| :-------|:-------|
<br />| 0.5     | 0.1    |
<br />| 0.25    | 0.01   |
<br />| 0.75    | 0.11   |
<br />If you have a number that repeats, stop after MAX DIGITS, which should be set as a global constant in your program. I suggest you start with MAX DIGITS = 8.
