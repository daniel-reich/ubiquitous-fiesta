
import re
def sigilize(desire):
    temp = ""
    desire = re.sub(r"[ AEIOU]+", r"", desire.upper())
    for c in desire[::-1]:
        if c not in temp:
            temp+=c
    return temp[::-1]

