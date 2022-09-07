"""
Day 8 - Caesar Cipher

This program consists in a encryption/decryption tool based on a letter shift.
"""
from art import logo

alphabet = ['a','b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
           'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't',
           'u', 'v', 'w', 'x', 'y', 'z']


def encrypt_message(message, offset):
    message = message.lower()
    encrypted_message = ''

    for index in range(len(message)):
        if message[index] in alphabet:
            char_index = (alphabet.index(message[index]) + offset) % len(alphabet)
            encrypted_message += alphabet[char_index]
        else:
            encrypted_message += message[index]
    
    print(f"Here is the encoded result: {encrypted_message}")


def decrypt_message(message, offset):
    message = message.lower()
    decrypted_message = ''

    for index in range(len(message)):
        if message[index] in alphabet:
            char_index = (alphabet.index(message[index]) - offset + len(alphabet)) % len(alphabet)
            decrypted_message += alphabet[char_index]
        else:
            decrypted_message += message[index]
    
    print(f"Here is the decoded result: {decrypted_message}")


if __name__ == "__main__":

    print(logo, end='\n\n')

    end_program = False
    while not end_program:

        command = input("Type 'encode' to encrypt, or type 'decode' to decrypt:\n").lower()
        message = input("Type your message:\n")
        offset = int(input("Type the shift number:\n"))

        if command == 'encode':
            encrypt_message(message, offset)
        elif command == 'decode':
            decrypt_message(message, offset)
        else:
            print("Command not found. Bye bye!")
            break

        go_again = input("Type 'yes' if you want to go again. Otherwise type 'no':\n").lower()

        if go_again == 'yes':
            print("\n")
        else:
            print("Program will be finished. Bye bye")
            end_program = True

        

