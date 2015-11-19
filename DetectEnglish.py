def loadDictionary():

    fileObj = open("dictionary.txt", "r")

    words = fileObj.read()

    englishwords = words.split("\n")

    #Split splits an string into arrays, /n new line character

    return englishwords

englishwords = loadDictionary()

input("\nPress the enter key to exit!")