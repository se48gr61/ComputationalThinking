userInput = input("Enter your Sentence: ").upper()
translated = ""
i = len(userInput)-1

while i >= 0:
    translated += userInput[i]
    i-=1
print(translated)