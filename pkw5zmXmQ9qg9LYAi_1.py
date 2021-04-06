
from re import sub
def space_message(txt):
    while "[" in txt:
        txt = sub(r"\[(\d)([A-Z]+)]",
                  lambda x: int(x.group(1)[0]) * x.group(2), txt)
    return txt

