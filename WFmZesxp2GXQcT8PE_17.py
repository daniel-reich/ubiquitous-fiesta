
def digital_cipher(message, key):
    alphas_lst = [chr(c) for c in range(ord('a'), ord('z')+1)]
    lst_keys = [alphas_lst.index(elem) + 1 for elem in message]
    len_key = len(str(key))
    times = len(lst_keys) // len_key
    idx = len(lst_keys) % len_key
    c = 0
    while times > 0:
        for i in range(len_key):
            adds = int(str(key)[i])
            lst_keys[c] += adds
            c += 1
        times -= 1
    lst_aux = lst_keys[::-1][:idx]
    for i in range(idx):
        lst_aux[i] += int(str(key)[i])
        lst_keys.pop(-1)
​
    return lst_keys + lst_aux

