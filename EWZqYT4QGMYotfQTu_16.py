
def tap_code(txt):
    code = [["a","b","c","d","e"],
            ["f","g","h","i","j"],
            ["l","m","n","o","p"],
            ["q","r","s","t","u"],
            ["v","w","x","y","z"]]
    if txt[0] == ".":
        txt = txt.split(" ")
        for i in range(0,len(txt)):
            if i%2 != 0:
                txt[i] = code[txt[i-1].count(".")-1][txt[i].count(".")-1]
                txt[i-1] = ""
        return "".join(txt)
    else:
        for element in txt:
            if element == "k":
                txt = txt.replace(element, ". ... ")
                continue
            for i in range(0,len(code)):
                if element in code[i]:
                    index = [i+1, code[i].index(element)+1]
                    txt = txt.replace(element, "."*(i+1)+" "+"."*(code[i].index(element)+1)+" ",1)
        return txt[:-1]

