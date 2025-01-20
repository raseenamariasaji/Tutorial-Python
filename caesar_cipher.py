# Caesar Cipher
print("1.Cipher Encryption\n2.Cipher Decryption")
print("-"*20)
choice = int(input("Enter your choice:"))
if choice==1:
    #Encryption
    message = input("Enter a message:")
    key = int(input("Enter key code:"))
    ciphertext = ""
    for ch in message:
        if ch.islower():  
            ordinalch = ord(ch)
            ordinalch += key
            if ordinalch > ord('z'):
                ordinalch = ord('a') + (ordinalch - ord('z')) - 1
            newch = chr(ordinalch)
            ciphertext += newch
        elif ch.isupper(): 
            ordinalch = ord(ch)
            ordinalch += key
            if ordinalch > ord('Z'):
                ordinalch = ord('A') + (ordinalch - ord('Z')) - 1
            newch = chr(ordinalch)
            ciphertext += newch
    print("Encrypted cipher text:", ciphertext)
elif choice==2:
    #Decryption
    ciphertext = input("Enter a ciphertext:")
    key = int(input("Enter key code:"))
    message = ""
    for ch in ciphertext:
        if ch.isalpha():  
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
            message += ch  
    print("Decrypted message is:", message)
else:
    print("INVALID INPUT!")