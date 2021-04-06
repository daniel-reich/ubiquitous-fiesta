
def truncate(txt, length):
    if " " not in txt[0:length]:
        return ""
    if length > len(txt):
        return txt
    if txt[length] == " ":
        return txt[0:length]
    marker = 0
    for i in range(length):
        if txt[i] == " ":
            marker = i
    return txt[0:marker]

