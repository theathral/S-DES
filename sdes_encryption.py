# sub-keys generation #
def __permutation(k, p):
    p_key = []
    for i in p:
        p_key.append(k[i])

    return p_key


def __rotate_left(k, n):
    k1 = k[:5]
    k2 = k[5:]

    r_k1 = k1[n:] + k1[:n]
    r_k2 = k2[n:] + k2[:n]

    return r_k1 + r_k2


# encryption #
def encryption(plain_text, key, p10, p8):
    cipher_p10 = __permutation(key, p10)
    r_cipher_1 = __rotate_left(cipher_p10, 1)
    r_cipher_2 = __rotate_left(r_cipher_1, 2)

    sub_key_1 = __permutation(r_cipher_1, p8)
    sub_key_2 = __permutation(r_cipher_2, p8)

    cipher_text = ""
    return cipher_text
