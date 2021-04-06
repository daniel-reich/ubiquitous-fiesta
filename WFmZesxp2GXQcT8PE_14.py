
def digital_cipher(message, key):
    lst_key = [int(c) for c in str(key)]
    len_key = len(lst_key)
    return [ord(c) - 96 + lst_key[i % len_key] for i, c in enumerate(message)]

