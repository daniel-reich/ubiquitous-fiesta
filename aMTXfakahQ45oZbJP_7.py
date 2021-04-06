
def complete_bracelet(lst):
    sub_seq, sub_seq_len, found = [], 2, False
    if len(lst) >= 4 and lst[:len(lst) // 2] == lst[len(lst) // 2:]:
        return True
    while sub_seq_len <= len(lst) // 2:
        if lst[:sub_seq_len] == lst[sub_seq_len: 2 * sub_seq_len]:
            sub_seq = lst[:sub_seq_len]
            found = True
            break
        else:
            sub_seq_len += 1
    if found:
        lst = lst[2 * sub_seq_len:]
        if lst:
            if not len(lst) % sub_seq_len:
                for i in range(len(lst) // sub_seq_len):
                    if sub_seq != lst[sub_seq_len * i:sub_seq_len * (i + 1)]:
                        return False
                return True
            else:
                return False
        else:
            return True
    return False

