# CS61002: Algorithms and Programming 1 
# Name: Davneet Kaur
# Date: Jan 19, 2016
# Lab#.py: Lab01



##### Template for assignments. Duplicate for appropriate number of exercises. ######

print "********** Exercise 1**********"

# Add your work for Exercise 1 here

# Program to print welcome message
print "Hello, My name is Davneet"
print "I am a student in CS10051"
print "Have a nice day!!"


print "********** Exercise 2**********"

# Add your work for Exercise 2 here

# Program to take user input
FirstName = raw_input ('Enter your first name: ')
LastName = raw_input ('Enter your last name: ')
print "Enter your date of birth"
Month = raw_input ('Month? ')
Day = raw_input ('Day? ')
Year = raw_input ('Year? ')
print FirstName + " " + LastName + " was born on " + Month + " " + Day + ", " + Year + "."


print "********** Exercise 3**********"

# Add your work for Exercise 3 here

#Pogram to calculate passer rating
#Precondition: All inputs to be given as Integers
PassCompletion = int(input ('Enter Pass completion: '))
PassAttempts = int(input ('Enter Pass attempts: '))
TotalPassingYards = int(input ('Enter Total Passing Yards: '))
TouchDowns = int(input ('Enter Touch downs: '))
Interceptions = int(input ('Eenter Intercepions: '))
C = ((PassCompletion/PassAttempts)*100-30)/20
Y = ((TotalPassingYards/PassAttempts)-3)/4
T = (TouchDowns/PassAttempts)*20
I = 2.375-((Interceptions/PassAttempts)*35)
PassRating = ((C+Y+T)/6)*100
print "Passer Rating is " + str(PassRating)
