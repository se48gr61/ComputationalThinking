import theseconddetectenglish
import transposition

#highscore
high = 0

correct_key = 2

#reads secret.txt

fileObj = open("secret.txt", "r")

ciphertext = fileObj.read()

for key in range(2, len(ciphertext)):

    message = transposition.decrypt(key, ciphertext)

    score = theseconddetectenglish.getEnglishCount(message)

    if score > high:

        high = score

        correct_key = key

    print("Key", key, "of", len(ciphertext), ":", score)

decrypted = transposition.decrypt(correct_key, ciphertext)

fileObj = open("secret.decrypted.txt", "w")

fileObj.write(decrypted)

fileObj.close()

print("Decrypted text written to secret.decrypted.txt")



