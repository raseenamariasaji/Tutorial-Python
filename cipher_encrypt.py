#Caesar Cipher Encryption
message = input("Enter a message:")
key = int(input("Enter key code:"))
ciphertext = ""
for ch in message:
    if ch.islower():  # Check if the character is a lowercase letter
        ordinalch = ord(ch)
        ordinalch += key
        if ordinalch > ord('z'):
            ordinalch = ord('a') + (ordinalch - ord('z')) - 1
        newch = chr(ordinalch)
        ciphertext += newch
    elif ch.isupper():  # Check if the character is an uppercase letter
        ordinalch = ord(ch)
        ordinalch += key
        if ordinalch > ord('Z'):
            ordinalch = ord('A') + (ordinalch - ord('Z')) - 1
        newch = chr(ordinalch)
        ciphertext += newch
print("Encrypted cipher text:", ciphertext)