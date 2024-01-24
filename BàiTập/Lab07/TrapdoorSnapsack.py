import numpy as np
import random

# Hàm sinh khóa
def generate_keys(N):
    a_prime = [random.randint(1,10) for _ in range(N)]
    m = random.randint(sum(a_prime)+1, 2*sum(a_prime))
    w = random.randint(2, m-1)
    a = [(w*i)%m for i in a_prime]
    return a_prime, m, w, a

# Hàm mã hóa
def encrypt(message, public_key):
    cipher = sum([message[i]*public_key[i] for i in range(len(message))])
    return cipher

# Hàm giải mã
def decrypt(cipher, private_key, w, m):
    w_inv = pow(w, -1, m)
    cipher_prime = (cipher * w_inv) % m
    message = []
    for i in reversed(private_key):
        if i <= cipher_prime:
            message.append(1)
            cipher_prime -= i
        else:
            message.append(0)
    message.reverse()
    return message

# Hàm chuyển chuỗi nhập vào thành mã nhị phân
def string_to_binary(message):
    binary_message = ' '.join(format(ord(char), '08b') for char in message)
    return binary_message

# Xử lí chuỗi thành binary measage 
message = input("Nhap chuoi message: ")
binary_message = string_to_binary(message)
binary_message = binary_message.replace(" ","")
N = len(binary_message)
binary_message = list(map(int, binary_message))

# Thực thi
a_prime, m, w, a = generate_keys(N)
cipher = encrypt(binary_message, a)
decrypted_message = decrypt(cipher, a_prime, w, m)

# In ra màn hình
print("Chuỗi ban đầu: ", message)
print("Mã hóa: ", cipher)
print("Giải mã: ", int(''.join(map(str,decrypted_message)), 2))