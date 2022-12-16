alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 
'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']
alphabet = alphabet * 3
direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))

def encrypt(text, shift):
    encryption = []
    final_encryption_numbers = []
    final_encryption_string = ""
    
    for index in text:
        encryption += index

    for start_encrypting in encryption:
        final_encryption_numbers = alphabet.index(start_encrypting) + shift
        final_encryption_string += alphabet[final_encryption_numbers]
    print(f"The encoded text is: {final_encryption_string}")


def decrypt(text, shift):
    decryption = []
    final_decryption_numbers = []
    final_decryption_string = ""
    
    for index in text:
        decryption += index

    for start_encrypting in decryption:
        final_decryption_numbers = alphabet.index(start_encrypting) - shift
        final_decryption_string += alphabet[final_decryption_numbers]
    print(f"The decoded text is: {final_decryption_string}")


if direction == "encode":
    encrypt(text, shift)
elif direction == "decode":
    decrypt(text, shift)