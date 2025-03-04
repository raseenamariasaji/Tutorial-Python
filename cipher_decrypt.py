#Caesar Cipher Decryption
ciphertext = input("Enter a ciphertext:")
key = int(input("Enter key code:"))
message = ""
for ch in ciphertext:
    if ch.isalpha():  # Check if the character is a letter
        ordinalch = ord(ch)
        ordinalch -= key
        if ch.islower():
            if ordinalch < ord('a'):
                ordinalch = ord('z') - (ord('a') - ordinalch - 1)
        elif ch.isupper():
            if ordinalch < ord('A'):
                ordinalch = ord('Z') - (ord('A') - ordinalch - 1)
        newch = chr(ordinalch)
        message += newch
    else:
        message += ch  # Keep non-letter characters unchanged
print("Decrypted message is:", message)
