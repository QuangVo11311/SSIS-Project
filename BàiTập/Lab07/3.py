import random

def generate_superincreasing_vector(N):
    a = [random.randint(1, 10)]
    for _ in range(1, N):
        a.append(random.randint(sum(a) + 1, 2 * sum(a)))
    return a

def generate_m_and_w(a):
    m = random.randint(sum(a) + 1, 2 * sum(a))
    w = random.randint(2, m - 1)
    return m, w

def generate_public_key(a, m, w):
    return [(w * ai) % m for ai in a]

def encrypt(public_key, plaintext):
    return sum(int(bit) * key for bit, key in zip(plaintext, public_key))

def decrypt(private_key, m, w, ciphertext):
    w_inv = pow(w, -1, m)
    c_prime = (ciphertext * w_inv) % m
    plaintext = []
    for ai in reversed(private_key):
        if ai <= c_prime:
            plaintext.append('1')
            c_prime -= ai
        else:
            plaintext.append('0')
    return ''.join(reversed(plaintext))

# Generate keys
N = 8
private_key = generate_superincreasing_vector(N)
m, w = generate_m_and_w(private_key)
public_key = generate_public_key(private_key, m, w)

# Encryption
plaintext = '10101010'
ciphertext = encrypt(public_key, plaintext)
print(f'Ciphertext: {ciphertext}')

# Decryption
decrypted_plaintext = decrypt(private_key, m, w, ciphertext)
print(f'Decrypted plaintext: {decrypted_plaintext}')
