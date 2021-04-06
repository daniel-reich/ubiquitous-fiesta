
def is_valid_phone_number(txt):
    c=""
    for i in txt:
        if i.isdigit():
            c+=i
    return len(c)==10 and  "({}) {}-{}".format(c[:3],c[3:6],c[6:])==txt

