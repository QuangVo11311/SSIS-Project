def find_key(plaintext, ciphertext):
    key = ''
    for p, c in zip(plaintext, ciphertext):
        if p.isalpha() and c.isalpha():
            shift = (ord(c.upper()) - ord(p.upper())) % 26
            key += chr(shift + ord('A'))
    return key

plaintext = "ANH AN COM"
ciphertext = "ERL MR GSY"

key = find_key(plaintext, ciphertext)
print("Khóa kết hợp:", key)

# To find the shortest repeating key, we can use the following function:
def shortest_repeating_key(key):
    key_length = len(key)
    for i in range(1, key_length):
        if key[:i]*(key_length//i) + key[:key_length%i] == key:
            return key[:i]
    return key

shortest_key = shortest_repeating_key(key)
print("Khóa gốc có độ dài ngắn nhất:", shortest_key)