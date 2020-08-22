# sub-keys generation #
def permutation(text, per):
    p_key = []
    for i in per:
        p_key.append(text[i])

    return p_key


def rotate_left(k, n):
    k1 = k[:5]
    k2 = k[5:]

    r_k1 = k1[n:] + k1[:n]
    r_k2 = k2[n:] + k2[:n]

    return r_k1 + r_k2


#
def xor(x, y):
    z = [0] * len(x)
    for i in range(len(x)):
        if x[i] != y[i]:
            z[i] = 1

    return z


def s_fun(text, s0, s1):

    return []


def fk(text, ep, s_key, s0, s1, p4):
    text_l = text[:4]
    text_r = text[4:]

    text_ep = permutation(text_r, ep)
    text_xor = xor(text_ep, s_key)
    text_s = s_fun(text_xor, s0, s1)
    text_p4 = permutation(text_s, p4)

    return xor(text_l, text_p4) + text_r


# encryption #
def encryption(plain_text, key, ip, ip_inv, ep, s0, s1, p10, p8, p4):
    cipher_p10 = permutation(key, p10)
    r_cipher_1 = rotate_left(cipher_p10, 1)
    r_cipher_2 = rotate_left(r_cipher_1, 2)

    sub_key_1 = permutation(r_cipher_1, p8)
    sub_key_2 = permutation(r_cipher_2, p8)

    print(sub_key_1)
    print(sub_key_2)

    plain_text_ip = permutation(plain_text, ip)
    first_loop = fk(plain_text_ip, ep, sub_key_1, s0, s1, p4)
    first_loop_inv = first_loop[4:] + first_loop[:4]
    second_loop = fk(first_loop_inv, ep, sub_key_2, s0, s1, p4)
    cipher_text = permutation(second_loop, ip_inv)

    return cipher_text
