def encrypt(plaintext, key):
    ciphertext = ""
    for char in plaintext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 + key) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 + key) % 26 + 97)
            ciphertext += shifted_char
        else:
            ciphertext += char
    return ciphertext

def decrypt(ciphertext, key):
    plaintext = ""
    for char in ciphertext:
        if char.isalpha():
            if char.isupper():
                shifted_char = chr((ord(char) - 65 - key) % 26 + 65)
            else:
                shifted_char = chr((ord(char) - 97 - key) % 26 + 97)
            plaintext += shifted_char
        else:
            plaintext += char
    return plaintext

key = 0
ciphertext = "sektvisfsoiupnhnunaahwjjhyzzbnwo"

for i in range(26):
    key += 1

    decrypted_text = decrypt(ciphertext, key)
    print("Decrypted text:", decrypted_text)
