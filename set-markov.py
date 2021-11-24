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
    dictionaryFile = "dictionary.json"
    inputFile = ""

    if numArguments >= 1:
        dictionaryFile = sys.argv[1]
    if numArguments >= 2:
        inputFile = sys.argv[2]

    return dictionaryFile, inputFile


# Clean up the string - keep only alpha numeric and spaces
def cleanString(inputString):
  txt = inputString.replace('\n', ' ')
  newText = re.sub('[^0-9a-zA-Z\s]+', '', txt)
  return newText


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
    tokens = input.split(" ")
    for i in range(0, len(tokens)-1):
        currentWord = tokens[i]
        nextWord = tokens[i+1]

        if currentWord not in dict:
            # Create a new entry in the dictonary
            dict[currentWord] = {nextWord: 1}
        else:
            allNextWords = dict[currentWord]

            if nextWord not in allNextWords:
                # Add new next state
                dict[currentWord][nextWord] = 1
            else:
                dict[currentWord][nextWord] = dict[currentWord][nextWord] + 1

    return dict


def updateFile(filename, dictionary):
    file = open(filename, "w")
    json.dump(dictionary, file)
    file.close()


# Start the program
main()