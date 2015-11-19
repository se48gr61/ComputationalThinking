import math

def encryptMessage(key, message) :

    ciphertext = [''] * key

    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)

def decryptTransposition(key, ciphertext):

    numOfRows = key

    numOfColumns = math.ceil(len(ciphertext) / key)

    numOfShadedBoxes = (numOfColumns * numOfRows) - len(ciphertext)

    plaintext = [""] * numOfColumns

    col = 0

    row = 0

    for symbol in ciphertext:

        plaintext[col] += symbol

        col += 1

        if (col == numOfColumns) or (col == numOfColumns-1 and row >= numOfRows - numOfShadedBoxes):

            col = 0

            row += 1
    return ''.join(plaintext)

def main():

    fileObj = open("text.encrypted.txt" , "r")

    ciphertext = fileObj.read()

    plaintext = decryptTransposition(120, ciphertext)

    fileObj.close()

    fileObj = open("text.decrypted.txt", "w")

    fileObj.write(plaintext)

    fileObj.close()

    print("Decrypted text written to text.decrypted.txt")

if __name__ == '__main__':
    main()
