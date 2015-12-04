#Own Project
numbers = "123456789101112"
userInput = input("Type a Number: ")

pos = numbers.find(userInput)
print(pos)

myString = "Done"
print(myString)

print("I have " + str(1) + " Basketball")

my_variable = input("Type in your message please").lower()
myString = " Your Message is being processed, displaying length and reversing word"
reverse = ""
i = len(my_variable)-1
while i >= 0:
    reverse += my_variable[i]
    i-=1
print(reverse)

from datetime import datetime
now = datetime.now()

print('%s/%s/%s %s:%s:%s' % (now.month, now.day, now.year, now.hour, now.minute, now.second))
name = input("What's your name? ")

if name == "Sergius":
    print("{} is a lumberjack and he's Ok!".format(name)).lower
else:
    print("{} Sleep's all night and {} work's all day".format(name, name)).upper

message = input("Hello Sir/Ma'am, please enter if you want to decrypt or encrypt oh and don't forget to choose your text!")

import transposition
import theseconddetectenglish


high = 0
correct_key = 2

fileObj = open("secret.txt", "r")

ciphertext = fileObj.read()

for key in range(2, len(ciphertext)):

    message = transposition.decrypt(key, ciphertext)
    score = theseconddetectenglish.getEnglishCount()

    if score > high:
        high = score
        correct_key = key
        print("Key,", key, "of", len(ciphertext), ":", score )

        decrypted = transposition.decrypt(correct_key, ciphertext)
        fileObj = open("secret.txt", "w")
        fileObj.write(decrypted)
        fileObj.close()
        print("Decrypted text written to secret.txt.decrypted.txt")

 # decrypt the message with every possible key

# check the score of each decryption

# if the score is higher than the previous high score then

# set that to the new high score

# set that key to the new correct key
# set the highest score to 0
# read content of secret.txt into a var
















