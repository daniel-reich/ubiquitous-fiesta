
def tap_code(text):
    dic =  {"A": ". .", "B": ". ..", "C": ". ...","K": ". ...", "D": ". ....", "E":". .....",
            "F": ".. .", "G":".. ..", "H":".. ...", "I":".. ....", "J":".. .....",
            "L":"... .", "M":"... ..", "N":"... ...", "O":"... ....", "P":"... .....",
            "Q":".... .", "R":".... ..", "S":".... ...", "T":".... ....", "U":".... .....",
            "V":"..... .", "W":"..... ..", "X":"..... ...", "Y":"..... ....", "Z":"..... ....."
            }
    r = ""
    if "." in text:
        dic = {v : k for k, v in dic.items() if k != "K"}
        e, one = "", False
        for i in text:
            if i == " " and one:
                r += dic[e].lower()
                e, one = "", False
            elif i == " ":
                one = True
                e += i
            else:
                e += i
        r += dic[e].lower() + " "         
    else:
        text = text.upper()
        for i in text:
            r += dic[i] + " "
    return r[:-1]

