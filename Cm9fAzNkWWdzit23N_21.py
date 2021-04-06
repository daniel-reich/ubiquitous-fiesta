
def wave(txt):
    lst = []
    for index, value in enumerate(txt):
        txt_lst = [i for i in txt]
        if txt_lst[index].isalpha():
            txt_lst[index] = txt_lst[index].upper()
            lst.append(''.join(txt_lst))
    return lst

