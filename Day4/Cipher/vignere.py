def resetter(num):
    return chr((num % 90) + (64 if num > 90 else 0))

def setter(num):
    return chr(num if num >= 65 else (num + 26))

def decrypt(ogText, key, encrypted):
    decrypted = ""
    for i in range(len(ogText)):
        index = i % len(key)
        update = ord(key[index]) - 65
        
        decrypted += setter((ord(encrypted[i]) - update))

    return decrypted

def encrypt(ogText, key):
    encrypted = ""
    for i in range(len(ogText)):
        index = i % len(key)
        update = ord(key[index]) - 65
        
        encrypted += resetter((ord(ogText[i]) + update))
    
    return encrypted


ogText = input("Enter the string to be encoded : ").upper()
key = input("Enter the key for encoding : ").upper()

finalResult = encrypt(ogText, key)
print(f"Encrypted Text: {finalResult}")

finalResult = decrypt(ogText, key, finalResult)
print(f"Decrypted Text: {finalResult}")