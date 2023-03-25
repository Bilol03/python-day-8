from ceaser_art import logo
print(logo)

end_game = False
alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(plain_text, plain_shift, direction):
    res = ""
    if direction == "decode":
        plain_shift *= -1

    for char in plain_text:
        if char in alphabet:
            index = alphabet.index(char)
            index += plain_shift
            res += alphabet[index]
        else:
            res += char

    print(f"Your {direction}d word is {res}")


while end_game != True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))

    if not end_game:
        caesar(plain_text=text, plain_shift=shift, direction=direction)
        end_game_ask = input("Dou you want to finish this game? Yes or No: ")
    if end_game_ask == "Yes" or end_game_ask == "yes":
        end_game = True
        print("Good Bye")
        break
    else:
        continue

while shift > 26:
    if shift % 2 == 0:
        shift = shift // 2
    elif shift % 3 == 0:
        shift = shift // 3
    else:
        shift = shift // 5

