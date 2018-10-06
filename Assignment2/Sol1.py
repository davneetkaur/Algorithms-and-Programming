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
