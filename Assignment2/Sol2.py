# Program to check if a number is divisible by 8
# Precondition: Input to be given as Integer
Number = int(input ('Enter a number: '))
if (Number % 8 == 0):
    print str(Number) + " is divisible by 8."
else:
    print str(Number) + " is not divisible by 8."
