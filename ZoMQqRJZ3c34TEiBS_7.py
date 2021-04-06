
def playfair(txt, keyword):
    key_upper = keyword.upper().replace('J', 'I')
    lst_key = sorted([c for c in set(key_upper)], key=key_upper.index)
    alphabet = list(chr(65 + i) for i in range(26) if chr(65 + i) != 'J')
    alphabet_no_key = sorted(list(set(alphabet) - set(lst_key)),
                             key=alphabet.index)
    polybius = lst_key + alphabet_no_key
​
    def coordinates(letter):
        idx = polybius.index(letter)
        return idx // 5, idx % 5
​
    def letter_by_row_col(r, c):
        return polybius[r * 5 + c]
​
    def digraphs(s):
        s = s.upper().replace('J', 'I')
        lst = [c for c in s if c.isalpha()]
        change = True
        while change:
            change = False
            for i in range(0, len(lst) - 1, 2):
                if lst[i] == lst[i + 1]:
                    lst = lst[: i + 1] + ['X'] + lst[i + 1:]
                    change = True
                    break
        if len(lst) % 2:
            lst.append('X')
        return lst
​
    res, shift = '', 1
    if ' ' in txt:
        lst_digraphs = digraphs(txt)
    else:
        lst_digraphs = [c for c in txt]
        shift = -1
    for i in range(0, len(lst_digraphs) - 1, 2):
        a_row, a_col = coordinates(lst_digraphs[i])
        b_row, b_col = coordinates(lst_digraphs[i + 1])
        if a_row == b_row:
            res += letter_by_row_col(a_row, (a_col + shift) % 5)
            res += letter_by_row_col(b_row, (b_col + shift) % 5)
        elif a_col == b_col:
            res += letter_by_row_col((a_row + shift) % 5, a_col)
            res += letter_by_row_col((b_row + shift) % 5, b_col)
        else:
            res += letter_by_row_col(a_row, b_col)
            res += letter_by_row_col(b_row, a_col)
    return res

