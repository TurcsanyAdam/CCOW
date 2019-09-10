def Cesar_cipher(code):
    Cipher = []
    Cipher1 = []
    for letter in code:
        Cipher.append(ord(letter)+3)
    for i in Cipher:
        Cipher1.append(chr(i))
    return Cipher1


print(Cesar_cipher("Codecool"))