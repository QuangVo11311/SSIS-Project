# Define the substitution dictionary
substitution_dict = {
    'a': 'q',
    'b': 'w',
    'c': 'e',
    'd': 'r',
    'e': 't',
    'f': 'y',
    'g': 'u',
    'h': 'i',
    'i': 'o',
    'j': 'p',
    'k': 'a',
    'l': 's',
    'm': 'd',
    'n': 'f',
    'o': 'g',
    'p': 'h',
    'q': 'j',
    'r': 'k',
    's': 'l',
    't': 'z',
    'u': 'x',
    'v': 'c',
    'w': 'v',
    'x': 'b',
    'y': 'n',
    'z': 'm'
}



# Function to encrypt the message
def encrypt_message(message):
    encrypted_message = ""
    for letter in message.lower():
        if letter in substitution_dict:
            encrypted_message += substitution_dict[letter]
        else:
            encrypted_message += letter
    return encrypted_message

# Function to decrypt the message
def decrypt_message(encrypted_message):
    decrypted_message = ""
    for letter in encrypted_message.lower():
        if letter in substitution_dict.values():
            for key in substitution_dict:
                if substitution_dict[key] == letter:
                    decrypted_message += key
        else:
            decrypted_message += letter
    return decrypted_message

#Nhập bản rõ
message = input('Nhập bản rõ: ')

#Mã hoá
encrypted_message = encrypt_message(message)
print("Mã hoá: ", encrypted_message)

#Giải mã
decrypted_message = decrypt_message(encrypted_message)
print("Giải mã: ", decrypted_message)