
def modify(txt):
    lst_idx = [c for c in range(ord('a')-96, ord('z')-95)]
    lst_ch = [chr(c) for c in range(ord('a'), ord('z')+1)]
    lst_zip = list(zip(lst_ch, lst_idx))
    lst_pos = []
    for ch in txt[::-1]:
        for elem in lst_zip:
            if elem[0] == ch:
                lst_pos.append(elem[1])
                break
    num = int(''.join(list(map(str, lst_pos))))
    num_bin = str(bin(num))[2:]
    return int(num_bin)

