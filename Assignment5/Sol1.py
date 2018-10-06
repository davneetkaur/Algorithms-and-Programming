# Program to do sequence alignment

def addIndel(string, index, lenString):
    if (index < 1 or index > lenString):
        print "Error! Index is out of range"
        print string
        return string
    else:
        modifiedString = string[0:index-1] + '-' + string[index:lenString+1]
        print modifiedString
        return modifiedString

def delIndel(string, originalString, index, lenString):
    if (index < 1 or index > lenString):
        print "Error! Index is out of range"
        print string
        return string
    else:
        if (string[index-1] != '-'):
            print "Error! Entered index is not an indel"
            print string
            return string
        else:
            modifiedString = string[0:index-1] + originalString[index-1] + string[index:lenString+1]
            print modifiedString
            return modifiedString

string1 = raw_input("Enter string one (A, T, C, G): ")
string2 = raw_input("Enter string two (A, T, C, G): ")

# retain original strings entered by user. this is needed while removing the indel
originalString1 = string1
originalString2 = string2

lenString1 = len(string1)
lenString2 = len(string2)

print "Choose any one option: "
print "'a' for add."
print "'d' for delete."
print "'s' for score." 
print "'q' for quit." 
userInput = raw_input("Enter choice: ")

while (userInput != 'q'):
    if (userInput == 'a'):
        strToChange = raw_input("Which string to add indel - 1 or 2?: ")
        if (strToChange == '1'):
            index = input("Enter index to place indel: ")
            string1 = addIndel(string1, index, lenString1)
        elif (strToChange == '2'):
            index = input("Enter index to place indel: ")
            string2 = addIndel(string2, index, lenString2)
        else:
            print "Please choose from '1' or '2'"

    elif (userInput == 'd'):
        strToChange = raw_input("Which string to delete indel - 1 or 2?: ")
        if (strToChange == '1'):
            index = input("Enter index to delete indel: ")
            string1 = delIndel(string1, originalString1, index, lenString1)
        elif (strToChange == '2'):
            index = input("Enter index to delete indel: ")
            string2 = delIndel(string2, originalString2, index, lenString2)
        else:
            print "Please choose from '1' or '2'"

    elif (userInput == 's'):
        # convert strings to upper case to compare
        string1 = string1.upper()
        string2 = string2.upper()
        
        match = 0
        mismatch = 0
        if (lenString1 < lenString2):                               # if string1 is shorter than string2, add indels to match length
            string1 = string1 + '-' * (len(string2) - len(string1))
        elif (lenString2 < lenString1):                             # if string2 is shorter than string1, add indels to match length
            string2 = string2 + '-' * (len(string1) - len(string2))
        for i in range (0,len(string1)):
            if ((string1[i] == '-') or (string2[i] == '-') or (string1[i] != string2[i])):
                mismatch += 1
            elif (string1[i] == string2[i]):
                match += 1
                # convert matching characters to lower case
                string1 = string1[0:i] + string1[i].lower() + string1[i+1:len(string1)+1]
                string2 = string2[0:i] + string2[i].lower() + string2[i+1:len(string2)+1]               
        print "Number of matches: ", match
        print "Number of mismatches: ", mismatch
        print "Strings: \n", string1, "\n", string2              

    else:
        print "Please choose from given options"

    # take user input until 'q' is entered
    userInput = raw_input("Enter choice again (a, d, s, q): ")
