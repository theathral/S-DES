import random
import sdes

# define variables
def_key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]  # 10-bit [0, 1]

ip = [1, 5, 2, 0, 3, 7, 4, 6]
ip_inv = [3, 0, 2, 4, 6, 1, 7, 5]
ep = [3, 0, 1, 2, 1, 2, 3, 0]
s0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],
      [0, 2, 1, 3],
      [3, 1, 3, 2]]
s1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],
      [3, 0, 1, 0],
      [2, 1, 0, 3]]
p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]  # 10-bit [0, 9]
p8 = [5, 2, 6, 3, 7, 4, 9, 8]  # 8-bit [0, 9]
p4 = [1, 3, 2, 0]


# key generation #
def key_gen(n):
    k = []
    for i in range(n):
        k.append(random.randint(0, 1))

    return k


plain_text = [1, 0, 0, 1, 0, 1, 1, 1]
print(plain_text)
key = key_gen(10)
ct = sdes.encryption(plain_text, key, ip, ip_inv, ep, s0, s1, p10, p8, p4)
print(ct)
pt = sdes.decryption(ct, key, ip, ip_inv, ep, s0, s1, p10, p8, p4)
print(pt)
