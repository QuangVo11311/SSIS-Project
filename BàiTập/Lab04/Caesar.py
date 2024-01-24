def caesar_cipher(text, shift):
    result = []
    
    for char in text:
        if 'A' <= char <= 'Z':  # Mã chữ HOA
            shifted_char = chr(((ord(char) - ord('A') + shift) % 26) + ord('A'))
        elif 'a' <= char <= 'z':  # Mã chữ thường
            shifted_char = chr(((ord(char) - ord('a') + shift) % 26) + ord('a'))
        else:
            shifted_char = char
        result.append(shifted_char)
    
    return ''.join(result)

def encrypt(text, key):
    return caesar_cipher(text, key)

def decrypt(text, key):
    return caesar_cipher(text, -key)

if __name__ == "__main__":
    text = input("Nhap vao van ban muon ma hoa: ")
    key = int(input("Nhap vao khoa dich chuyen k: "))
    
    encrypted_text = encrypt(text, key)
    decrypted_text = decrypt(encrypted_text, key)
    
    print("Văn bản ban đầu: " + text)
    print("Văn bản đã mã hóa: " + encrypted_text)
    print("Văn bản đã giải mã: " + decrypted_text)