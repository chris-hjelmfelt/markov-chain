import sys
import json
import os
import re

def main():
    dictionaryFile, inputFile = readArguments()
    dictionary = loadDictionary(dictionaryFile)

    if inputFile == "":
        # Interactive Mode
        while True:
            userInput = input(">> ")
            if userInput == "":
                break
            newText = cleanString(userInput)
            dictionary = learn(dictionary, newText)
            updateFile(dictionaryFile, dictionary)
    else:
        # Read from File
        f = open(inputFile, "r", encoding='utf-8')
        fileInput = f.read()         
        f.close()
        newText = cleanString(fileInput)  
        dictionary = learn(dictionary, newText)
        updateFile(dictionaryFile, dictionary)



def readArguments():
    numArguments = len(sys.argv) - 1
    dictionaryFile = "dictionary2.json"
    inputFile = ""

    if numArguments >= 1:
        dictionaryFile = sys.argv[1]
    if numArguments >= 2:
        inputFile = sys.argv[2]

    return dictionaryFile, inputFile


# Clean up the string - keep only alpha numeric and spaces
def cleanString(inputString):
  txtLine = inputString.replace('\n', ' ')  
  txtAlpha = re.sub('[^0-9a-zA-Z\s]+', '', txtLine)
  txtSpace = txtAlpha.replace(' ', '_')
  return txtSpace


def loadDictionary(filename):
    if not os.path.exists(filename):  # Create a json file
        file = open(filename, "w")
        json.dump({}, file)
        file.close()

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary


def learn(dict, input):
    for i in range(3, len(input)-1):
        currentL = input[i-3] + input[i-2] + input[i-1] + input[i]        
        nextL = input[i+1]

        if currentL not in dict:
            # Create a new entry in the dictonary
            dict[currentL] = {nextL: 1}
        else:
            allNextWords = dict[currentL]

            if nextL not in allNextWords:
                # Add new next state
                dict[currentL][nextL] = 1
            else:
                dict[currentL][nextL] = dict[currentL][nextL] + 1

    return dict


def updateFile(filename, dictionary):
    file = open(filename, "w")
    json.dump(dictionary, file)
    file.close()


# Start the program
main()