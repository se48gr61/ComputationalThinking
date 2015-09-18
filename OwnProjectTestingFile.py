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













