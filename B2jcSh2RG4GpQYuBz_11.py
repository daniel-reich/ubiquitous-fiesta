
def is_valid_phone_number(txt):
    return (txt[0] =="(" and txt[4]==")" and txt[5]==" " and txt[9]=="-" and len(txt)==14)

