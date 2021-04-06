
def tune(lst):
    freq = [329.63, 246.94, 196, 146.83, 110, 82.41]
    result = []
    off = 0
    
    for i in range(len(lst)):
        off = round(((lst[i] / freq[i]) - 1) * 100)
        if lst[i] == 0:
            result.append(" - ")
        elif off == 0:
            result.append("OK")
        elif off > 0:
            if off <= 2:
                result.append("+<")
            else:
                result.append("+<<")
        else:
            if off >= - 2:
                result.append(">+")
            else:
                result.append(">>+")
    return result

