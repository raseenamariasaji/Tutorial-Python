# Caesar Cipher
message = input("Enter a message(in small letters):")
key = int(input("Enter key code:"))
ciphertext =" "
for ch in message:
    ordinalch = ord(ch)
    ordinalch += key
    if ordinalch > ord('z'):
        ordinalch = ord('a')+ (ordinalch- ord('z'))-1
    newch = chr(ordinalch)
    ciphertext += newch    
print("Encrypted cipher text:",ciphertext) 