import os
import random
import sdes
import time

# define variables
def_key = [1, 0, 1, 0, 0, 0, 0, 0, 1, 0]  # 10-bit [0, 1]

ip = [1, 5, 2, 0, 3, 7, 4, 6]  # IP table - 8-bit [0, 7]
ip_inv = [3, 0, 2, 4, 6, 1, 7, 5]  # Inverted IP table - 8-bit [0, 7]
ep = [3, 0, 1, 2, 1, 2, 3, 0]  # EP table - 8-bit [0, 7]
s0 = [[1, 0, 3, 2],
      [3, 2, 1, 0],  # S0 matrix
      [0, 2, 1, 3],
      [3, 1, 3, 2]]
s1 = [[0, 1, 2, 3],
      [2, 0, 1, 3],  # S1 matrix
      [3, 0, 1, 0],
      [2, 1, 0, 3]]
p10 = [2, 4, 1, 6, 3, 9, 0, 8, 7, 5]  # P10 table - 10-bit [0, 9]
p8 = [5, 2, 6, 3, 7, 4, 9, 8]  # P8 table - 8-bit [0, 9]
p4 = [1, 3, 2, 0]  # P4 table - 4-bit [0, 3]


# key generation #
def bit_gen(n):
    k = []
    for i in range(n):
        k.append(random.randint(0, 1))

    return k


plain_text = [1, 0, 0, 1, 0, 1, 1, 1]
print(plain_text)
ct = sdes.encryption(plain_text, def_key, ip, ip_inv, ep, s0, s1, p10, p8, p4)
print(ct)
pt = sdes.decryption(ct, def_key, ip, ip_inv, ep, s0, s1, p10, p8, p4)
print(pt)

while True:
    run = input("Do you want to run multiple random tests? (Y/n): ")
    if run == "N" or run == "n":
        exit(0)
    elif run == "Y" or run == "y":
        break
    else:
        continue

loops = 0
while True:
    try:
        loops = int(input("How many? (>= 1000) "))
        if not loops >= 1000:
            raise ValueError
        break
    except ValueError:
        continue

print("\nStart testing:")

flag = True
start_time = time.time()
for loop in range(loops):
    plain_text = bit_gen(8)
    key = bit_gen(10)

    ct = sdes.encryption(plain_text, key, ip, ip_inv, ep, s0, s1, p10, p8, p4)
    pt = sdes.decryption(ct, key, ip, ip_inv, ep, s0, s1, p10, p8, p4)

    if plain_text != pt:
        print("Plain text: ", str(plain_text))
        print("Encryption: ", str(ct))
        print("Decryption: ", str(pt))
        flag = False
    else:
        if loop % (loops // 10) == (loops // 10) - 1:
            print(".", loop + 1)
        elif loop % (loops // 1000) == (loops // 1000) - 1:
            print(".", end="")

print("\nEnd testing... ", end="")

if flag:
    print("OK!")
else:
    print("Something went wrong!")

end_time = time.time()
print("Time elapsed: ", end_time - start_time)

os.system("pause")
