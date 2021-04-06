
import re
def space_message(txt):
    x = re.findall(r'\[\w+\]',txt)
    if len(x) == 0:
        return txt
    num = re.findall(r'(?<=\[)\d+(?=\w+\])',txt)
    letters = re.findall(r'(?<=\d)[A-Z]+(?=\])',txt)
    subs = [j * int(i) for i,j in zip(num,letters)]
    for i in range(len(x)):
        txt = txt.replace(x[i],subs[i])
    return space_message(txt)

