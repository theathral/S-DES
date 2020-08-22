import random
import sdes_encryption

# define variables
def_key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]  # 10-bit [0, 1]
p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]  # 10-bit [0, 9]
p8 = [5, 2, 6, 3, 7, 4, 9, 8]  # 8-bit [0, 9]


# key generation #
def key_gen(n):
    k = []
    for i in range(n):
        k.append(random.randint(0, 1))

    return k


plain_text = []
sdes_encryption.encryption(plain_text, def_key, p10, p8)
