# CS61002: Algorithms and Programming 1 
# Name: Davneet Kaur
# Date: April 9, 2017
# Project1.py



##### Template for Project. ######

print ("********** Project**********")

# Add your work here

import glob
import random

def createDict(selection):
    with open(selection) as af:
        dict = af.read()
        words = dict.strip().split("\n")
        dictionary = {}
        for i in words:
            (word,meaning) = i.split(":")
            dictionary[word] = meaning
    af.close()
    return dictionary

def quize(dictionary, eng, spanish):
    if (spanish == dictionary[eng]):
        return True
    else:
        return False

def writeWord(dictionary, eng):
    with open("wrong.txt","a") as af:
        af.write(eng)
        af.write(":")
        af.write(dictionary[eng])
        af.write("\n")
    af.close()

##1
fileList = glob.glob("*.txt")
if (len(fileList) == 0):
    print("Error! No files in the current directory")
    exit()
for files in fileList:
    print(files)

##2
selection = raw_input("Enter choice: ")
while (selection not in fileList):
    print("Please enter a valid choice")
    selection = raw_input("Enter choice again: ")

##3
dictionary = createDict(selection)

##4
print("No. of words in selected file: "), len(dictionary)

##5
nWords = int(raw_input("Enter number of words you want to be quizzed for: "))
while (nWords < 1 or nWords > len(dictionary)):
       print("Please enter a valid number less than "), len(dictionary)
       nWords = int(raw_input("Enter number of words again: "))

##6
wordsList = random.sample(dictionary, nWords)
print("Enter Spanish for below English words:")
for i in range(0, len(wordsList)):
    eng = wordsList[i]
    print( eng,":")
    spanish = raw_input()
    result = quize(dictionary, eng, spanish)

    ##7
    if result == False:
        print("You gave a wrong answer.")
        uChoice = raw_input("Would you like to save word for review? (Y/N): ")
        if uChoice == 'Y' or uChoice == 'y':
            writeWord(dictionary, eng)
