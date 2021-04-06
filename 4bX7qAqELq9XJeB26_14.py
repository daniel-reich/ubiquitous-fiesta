
def to_camel_case(txt):
    txt=txt.split("_") if "_" in txt else txt.split("-")
    return "".join([txt[0]] + [w.title() for w in txt[1:]])

