message = input("Enter your sentence:")
key = 13
mode = input("Do you want to encrypt or decrypt?")
mode=mode.strip(' ')
print(mode)
letters ="ABCDEFGHIJKLMNOPQRSTUVWXYZ"
translated = ""
message = message.upper()
for symbol in message:
    if symbol in letters:
        num = letters.find(symbol)
        if mode == 'encrypt':
            num = num+key
        elif mode == "decrypt":
            num = num-key

        if num >= len(letters):
            num = num-len(letters)
        elif num < 0:
            num = num+len(letters)

        translated = translated+letters[num]

    else:
        translated = translated+symbol

print(translated)




