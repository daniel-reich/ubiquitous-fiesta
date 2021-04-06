
def text_to_number_binary(txt):
    a = [i.lower() for i in list(txt.split()) if i.lower() in ("zero", "one")]
    txt = "".join(a[:8*(len(a)//8)])
    txt = txt.replace("zero", "0")
    txt = txt.replace("one", "1")
    return txt

