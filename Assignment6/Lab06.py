# CS61002: Algorithms and Programming 1 
# Name: Davneet Kaur
# Date: April 13, 2017
# Lab#.py: Assignment# 6




print "********** Exercise 1 **********"


# Program to generate Pascal's Triangle

## Part 1
def make_new_row(oldRow):
    if oldRow == []:
        newRow = [1]
        return newRow
    elif oldRow == [1]:
        newRow = [1,1]
        return newRow
    else:
        newRow = []
        lenOldRow = len(oldRow)
        newRow.append(1)
        for i in range(lenOldRow-1):
            newRow.append(oldRow[i] + oldRow[i+1])
        newRow.append(1)
        return newRow


##Part 2
print "********** Part 2 **********"

height = int(raw_input("Enter the desired height of Pascal's triangle: "))
oldRow = []
for i in range(height):
    newRow = make_new_row(oldRow)
    print newRow
    oldRow = newRow


##Part 3
print "********** Part 3 **********"

height = int(raw_input("Enter the desired height of Pascal's triangle: "))
oldRow = []
masterList = []
for i in range(height):
    newRow = make_new_row(oldRow)
    masterList.append(newRow)
    oldRow = newRow

print "Printing whole list of lists:"
print masterList

print "Printing list of lists, one list at a time:"
lenMList = len(masterList)
for i in range(lenMList):
    print masterList[i]
