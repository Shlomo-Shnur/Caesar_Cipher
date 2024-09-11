from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def encrypt(original_text, shift_amount):
    encrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            encrypted_text += letter
            continue
        index = alphabet.index(letter)
        encrypted_text += alphabet[(index + shift_amount) % len(alphabet)]
    print(f"Here is the encoded result: {encrypted_text}")


def decrypt(original_text, shift_amount):
    decrypted_text = ""
    for letter in original_text:
        if letter not in alphabet:
            decrypted_text += letter
            continue
        index = alphabet.index(letter)
        decrypted_text += alphabet[(index - shift_amount) % len(alphabet)]
    print(f"Here is the decoded result: {decrypted_text}")


def caesar(direction_input, text_input, shift_input):
    if direction_input == "encode":
        encrypt(text_input, shift_input)
    elif direction_input == "decode":
        decrypt(text_input, shift_input)


print(logo)
while True:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(direction, text, shift)
    keep_going = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n").lower()
    if keep_going == "no":
        print("Goodbye!")
        break
