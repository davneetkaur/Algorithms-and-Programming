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
