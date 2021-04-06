
def checkdup(str):
    result = False
    if len(str) == 1:
        return False
    for i in range(len(str) - 1):
        if str[i] == str[i + 1]:
            result = True
    return result
​
​
def super_reduced_string(txt):
    result = ""
    count = 1
    while checkdup(txt):
        for i in range(len(txt) - 1):
            if txt[i] == txt[i + 1]:
                count += 1
            else:
                if count % 2 == 1:
                    result = result + txt[i]
                count = 1
            if i == len(txt)-2 and count > 1:
                if count % 2 == 1:
                    result = result + txt[i]
        if txt[-1] != txt[-2]:
            result = result + txt[-1]
        txt = result
        result = ""
​
    return "Empty String" if txt == "" else txt

