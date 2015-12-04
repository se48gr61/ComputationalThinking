def loadDictionary():
    dictionaryFile = open('dictionary.txt')
    return dictionaryFile.read().split('\n')

def getEnglishCount(message):
    ENGLISH_WORDS = loadDictionary()
    message = message.upper()
    message = removeNonLetters(message)
    possibleWords = message.split()
    if possibleWords == []:
        return 0.0  # no words at all, so return 0.0
    matches = 0
    for word in possibleWords:
        if word in ENGLISH_WORDS:
            matches += 1
    return float(matches) / len(possibleWords)

def removeNonLetters(message):
    UPPERLETTERS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    LETTERS_AND_SPACE = UPPERLETTERS + UPPERLETTERS.lower() + ' \t\n'
    lettersOnly = ""
    for symbol in message:
        if symbol in LETTERS_AND_SPACE:
            lettersOnly += symbol
    return lettersOnly