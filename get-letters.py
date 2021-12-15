import sys
import json
import os
import random

def main():
    length, filename = readArguments()
    dictionary = loadDictionary(filename)

    lastLetter = None
    result = ""
    for i in range(0, length):
        newLetter = getNextLetter(lastLetter, dictionary)
        result = result + newLetter
        lastLetter = newLetter
    
    print(result)


def readArguments():
    length = 50
    filename = "dictionary2.json"

    numArguments = len(sys.argv) - 1
    if numArguments >= 1:
        length = int(sys.argv[1])
    if numArguments >= 2:
        filename = sys.argv[2]

    return length, filename



def loadDictionary(filename):
    if not os.path.exists(filename):  
        sys.exit("Error: Dictionary file not found")

    file = open(filename, "r")
    dictionary = json.load(file)
    file.close()
    return dictionary


def getNextLetter(lastLetter, dict):
    if lastLetter in dict:
        # Pick next Letter from list
        candidates = dict[lastLetter]
        candidatesNormalized = []

        for Letter in candidates:
            freq = candidates[Letter]
            for i in range(0, freq):
                candidatesNormalized.append(Letter)
            
        rnd = random.randint(0, len(candidatesNormalized)-1)
        return candidatesNormalized[rnd]

    else:
        # Pick new random state
        newLetter = pickRandom(dict)
        return newLetter


def pickRandom(dict):
    randNum = random.randint(0, len(dict)-1)
    newLetter = list(dict.keys())[randNum]
    return newLetter


main()