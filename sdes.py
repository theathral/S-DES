# Permutation of a "text" with "per" table
def permutation(text, per):
    p_key = []
    for i in per:
        p_key.append(text[i])

    return p_key


# Swift left of a "k" text by "n" bits
def rotate_left(k, n):
    k1 = k[:5]
    k2 = k[5:]

    r_k1 = k1[n:] + k1[:n]
    r_k2 = k2[n:] + k2[:n]

    return r_k1 + r_k2


# XOR execution of "x" and "y" lists
def xor(x, y):
    z = [0] * len(x)
    for i in range(len(x)):
        if x[i] != y[i]:
            z[i] = 1

    return z


# S-box mapping of a "text" into a matrix "s" (single box)
def s_box(text, s):
    row = int(str(text[0]) + str(text[3]), 2)  # First and last bit
    col = int(str(text[1]) + str(text[2]), 2)  # 2nd and 3rd bit

    return [int(i) for i in str("{0:b}".format(s[row][col])).zfill(2)]


# S-box mapping of a "text" into matrices "s0" & "s1"
def s_fun(text, s0, s1):
    text_l = text[:4]
    text_r = text[4:]

    s_box_l = s_box(text_l, s0)
    s_box_r = s_box(text_r, s1)

    return s_box_l + s_box_r


def fk(text, ep, s_key, s0, s1, p4):
    text_l = text[:4]  # L-half of text
    text_r = text[4:]  # R-half of text

    text_ep = permutation(text_r, ep)  # Permutation of R-half with EP table
    text_xor = xor(text_ep, s_key)  # XOR with sub-key
    text_s = s_fun(text_xor, s0, s1)  # S-boxes function execution
    text_p4 = permutation(text_s, p4)  # Permutation with P4 table

    return xor(text_l, text_p4) + text_r  # XOR with L-half and concat with initial R-half


# encryption #
def encryption(plain_text, key, ip, ip_inv, ep, s0, s1, p10, p8, p4):
    # Generation of K1 & K2 keys
    cipher_p10 = permutation(key, p10)  # Permutation with P10 table
    r_cipher_1 = rotate_left(cipher_p10, 1)  # Shift left
    r_cipher_2 = rotate_left(r_cipher_1, 2)  # Shift left

    sub_key_1 = permutation(r_cipher_1, p8)  # Generation of K1 by permutation with P8 table
    sub_key_2 = permutation(r_cipher_2, p8)  # Generation of K2 by permutation with P8 table

    # Encryption of the plain text
    plain_text_ip = permutation(plain_text, ip)  # Initial permutation with IP table
    first_loop = fk(plain_text_ip, ep, sub_key_1, s0, s1, p4)  # fK1 execution
    first_loop_inv = first_loop[4:] + first_loop[:4]  # Switch function execution
    second_loop = fk(first_loop_inv, ep, sub_key_2, s0, s1, p4)  # fK2 execution
    cipher_text = permutation(second_loop, ip_inv)  # Final permutation with inverted IP table

    return cipher_text


# decryption #
def decryption(cipher_text, key, ip, ip_inv, ep, s0, s1, p10, p8, p4):
    # Generation of K1 & K2 keys
    cipher_p10 = permutation(key, p10)  # Permutation with P10 table
    r_cipher_1 = rotate_left(cipher_p10, 1)  # Shift left
    r_cipher_2 = rotate_left(r_cipher_1, 2)  # Shift left

    sub_key_1 = permutation(r_cipher_1, p8)  # Generation of K1 by permutation with P8 table
    sub_key_2 = permutation(r_cipher_2, p8)  # Generation of K2 by permutation with P8 table

    # Decryption of the plain text
    cipher_text_ip = permutation(cipher_text, ip)  # Initial permutation with IP table
    first_loop = fk(cipher_text_ip, ep, sub_key_2, s0, s1, p4)  # fK2 execution
    first_loop_inv = first_loop[4:] + first_loop[:4]  # Switch function execution
    second_loop = fk(first_loop_inv, ep, sub_key_1, s0, s1, p4)  # fK1 execution
    plain_text = permutation(second_loop, ip_inv)  # Final permutation with inverted IP table

    return plain_text
