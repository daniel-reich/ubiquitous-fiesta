
def text_to_number_binary(txt):
    txt = txt.lower()
    list_txt = txt.split()
    str_txt = ''
    for ele in list_txt:
        if ele == 'one':
            str_txt += '1'
        elif ele == 'zero':
            str_txt += '0'
    if len(str_txt) % 8 == 0:
        return str_txt
    else:
        return str_txt[0:len(str_txt)-len(str_txt) % 8]

