userInput = input("Enter your sentence: ")
vowels = "AEIOUaeiou"

displayVowels = ""
displayConsonants = ""

for letter in userInput:
    if letter in vowels:
        displayVowels = displayVowels + letter
    else:
        displayConsonants = displayConsonants + letter


print("Vowels: " + displayVowels)
print("Consonants: " + displayConsonants)
