import sys


def main():
    dictionaryFile, inputFile = readArguments()
    dictionary = loadDictionary(dictionaryFile)

    if inputFile == "":
        # Interactive Mode

    else:
        # Read from File



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
