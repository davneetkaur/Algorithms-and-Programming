# CS61002: Algorithms and Programming 1 
# Name: Davneet Kaur
# Date: Jan 26, 2017
# Lab#.py: Assignment# 2



##### Template for assignments. Duplicate for appropriate number of exercises. ######

print "********** Exercise 1**********"

# Add your work for Exercise 1 here

# Program to take input from user and check conditions
# Precondition: Full month name should be entered and the first letter should be capital. Date should be entered till December 31, 2016. Leap year dates should not be eneterd.
FirstName = raw_input ('Enter your first name: ')
LastName = raw_input ('Enter your last name: ')
print "Enter your date of birth"
Month = raw_input ('Month? ')
Day = int(input ('Day? '))
Year = int(input ('Year? '))
if (Month == 'January' or Month == 'March' or Month == 'May' or Month == 'July' or Month == 'August' or Month == 'October' or Month == 'December') and (Day not in range(1,32)):
    print "Invalid Information"
elif (Month == 'April' or Month == 'June' or Month == 'September' or Month == 'November') and (Day not in range(1,31)):
    print "Invalid Information"
elif (Month == 'February') and (Day not in range(1,29)):
    print "Invalid Information"
elif (Year > 2016):
    print "Invalid Information"
else:
    print FirstName + " " + LastName + " was born on " + Month + " " + str(Day) + ", " + str(Year) + "."


print "********** Exercise 2**********"

# Add your work for Exercise 2 here

# Program to check if a number is divisible by 8
# Precondition: Input to be given as Integer
Number = int(input ('Enter a number: '))
if (Number % 8 == 0):
    print str(Number) + " is divisible by 8."
else:
    print str(Number) + " is not divisible by 8."
