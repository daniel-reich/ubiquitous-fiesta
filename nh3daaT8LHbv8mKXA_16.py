
def text_to_num(phone):
    chars_to_change = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    replace_with = "22233344455566677778889999"
    table = phone.maketrans(chars_to_change, replace_with)
    return phone.translate(table)

