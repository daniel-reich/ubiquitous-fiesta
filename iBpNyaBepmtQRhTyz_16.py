
def c_cipher(msg, keyword):
    len_key = len(keyword)
    sorted_key = sorted(keyword)
    if msg[0].isupper() or ' ' in msg:
        lower_msg = ''.join(c.lower() for c in msg
                            if c.isalpha() or c.isdigit())
        len_lower_msg = len(lower_msg)
        remainder_xxx = len_lower_msg % len_key
        n_rows = len_lower_msg // len_key
        if remainder_xxx:
            n_rows += 1
            lower_msg += 'x' * (len_key - remainder_xxx)
        msg_lst = [lower_msg[i * len_key: i * len_key + len_key]
                   for i in range(n_rows)]
        return ''.join(''.join(msg_lst[i][keyword.index(sorted_key[j])]
                               for i in range(n_rows))
                       for j in range(len_key))
    else:
        n_rows = len(msg) // len_key
        msg_lst = [msg[i * n_rows: i * n_rows + n_rows]
                   for i in range(len_key)]
        return ''.join(''.join(msg_lst[sorted_key.index(keyword[j])][i]
                               for j in range(len_key))
                       for i in range(n_rows))

