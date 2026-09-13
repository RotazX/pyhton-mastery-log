
int - an integer, used for whole numbers and calculations
float - a decimal number, also used in calculations
str - a string of text; str + str combines two strings
bool - a Boolean value: True or False

input() always returns a string because everything typed into a program arrives as text.

Writing int("abc") gives a ValueError because Python cannot convert "abc" to an integer. "25" is a string, while 25 is an integer; they contain similar text, but they are different types.

5 / 2 returns a float: 2.5, whereas 5 // 2 returns an integer: 2.

