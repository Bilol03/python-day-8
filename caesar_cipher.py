alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))



def ceasar(plain_text, plain_shift, direction):
    res = ""

    for i in plain_text:
        index = alphabet.index(i)

        if direction == "decode":
            plain_shift *= -1
        index += plain_shift
        res += alphabet[index]
        plain_shift *= -1

    print(f"Your {direction}d word is {res}")

ceasar(direction=direction, plain_text=text, plain_shift=shift)