import sys
import json
import os


def main():
    dictionaryFile, inputFile = readArguments()
    dictionary = loadDictionary(dictionaryFile)

    if inputFile == "":
        # Interactive Mode
        while True:
            userInput = input(">> ")
            if userInput == "":
                break

            dictionary = learn(dictionary, userInput)
            updateFile(dictionaryFile, dictionary)
    else:
        # Read from File
        print("Not yet implemented")



def readArguments():
    numArguments = len(sys.argv) - 1
    dictionaryFile = "dictionary.json"
    inputFile = ""

    if numArguments >= 1:
        dictionaryFile = sys.argv[1]
    if numArguments >= 2:
        inputFile = sys.argv[2]

    return dictionaryFile, inputFile


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