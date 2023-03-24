alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(plain_text, plain_shift):
    res = ""
    for i in plain_text:
        index = alphabet.index(i)
        index += plain_shift
        res += alphabet[index]
    print(res)

def decrypt(plain_text, plain_shift):
    res = ""
    for i in plain_text:
        index = alphabet.index(i)
        index -= plain_shift
        res += alphabet[index]
    print(res)

if direction == "encode":
    encrypt(plain_text=text, plain_shift=shift)
else:
    decrypt(plain_text=text, plain_shift=shift)