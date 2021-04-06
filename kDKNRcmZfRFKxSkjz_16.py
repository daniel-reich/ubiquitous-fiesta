
def unmix(txt):
    result = []
    if len(txt) % 2 == 0:
       for i in range(0, len(txt), 2):
           result.append(txt[i+1])
           result.append(txt[i])
    elif len(txt) % 2 != 0:
       for i in range(0, len(txt)-1, 2):
           result.append(txt[i+1])
           result.append(txt[i])
       result.append(txt[len(txt)-1])
    return "".join(result)

