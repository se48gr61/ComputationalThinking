import math


def encrypt(key, message):
    # Each string n ciphertext represents a column in the grid.
    ciphertext = [""] * key
    for col in range(key):
        pointer = col
        while pointer < len(message):
            ciphertext[col] += message[pointer]
            pointer += key
    return ''.join(ciphertext)


def decrypt(key, ciphertext):
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
    fileObj = open('text.encrypted.txt', 'r')
    ciphertext = fileObj.read()
    fileObj.close()
    message = decrypt(765, ciphertext)
    print(message)

if __name__ == "__main__":
    main()
