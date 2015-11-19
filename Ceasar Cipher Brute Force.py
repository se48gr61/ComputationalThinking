# Ask user for encrypted input

message = input("Enter an encrypted message: ")

#Convert the message to uppercase

message = message.upper()

#Alphabet

letters = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

#Try every possible key in range of 1 to 26

for key in range(1, 27):

    #Variable that stores the translated phrase

    decrypted = ""

    print(key)

#For every key: decrypt using the key

    for symbol in message:

    #if the symbol is a letter

        if symbol in letters:
            number = letters.find(symbol)
            number -= key
        if number < 0:
            number += 26
        decrypted += letters[number]

            #display the decrypted output to the user

    print(decrypted)











