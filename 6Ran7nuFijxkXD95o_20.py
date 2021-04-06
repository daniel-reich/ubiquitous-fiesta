
def keyboard_shortcut(txt):
    txt_split = txt.split()
    result = []
    to_copy = ''
    for i in range(len(txt_split)):
        if txt_split[i] == "Ctrl" and txt_split[i+1] == "+" and  txt_split[i+2] == "C":
            to_copy = ""
            for j in range(0, i):
                if txt_split[j] != "Ctrl" and txt_split[j] != "+" and txt_split[j] != "C" and txt_split[j] != "V":
                    to_copy += txt_split[j] + " "
            txt_split[i] = to_copy.rstrip()
        elif txt_split[i] == "Ctrl" and txt_split[i+1] == "+" and  txt_split[i+2] == "V" and to_copy != "":
              result.append(to_copy.rstrip())
              to_copy = ''
        elif txt_split[i] != "Ctrl" and txt_split[i] != "+" and  txt_split[i] != "C" and txt_split[i] != "V":
            result.append(txt_split[i])
    return " ".join(result)

