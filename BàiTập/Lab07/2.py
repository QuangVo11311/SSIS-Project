import numpy as np
import random

def generate_keys(N):
    a_prime = [random.randint(1,10) for _ in range(N)]
    m = random.randint(sum(a_prime)+1, 2*sum(a_prime))
    w = random.randint(2, m-1)
    a = [(w*i)%m for i in a_prime]
    return a_prime, m, w, a

def encrypt(message, public_key):
    cipher = sum([message[i]*public_key[i] for i in range(len(message))])
    return cipher

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

N = 8
message = [random.randint(0,1) for _ in range(N)]
print(type(message))
a_prime, m, w, a = generate_keys(N)
cipher = encrypt(message, a)
decrypted_message = decrypt(cipher, a_prime, w, m)

print("Original Message: ", message)
print("Cipher: ", cipher)
print("Decrypted Message: ", decrypted_message)