
def max_separator(txt):
    copy = txt[:]
    high = {}
    for let in txt:
        copy = copy.replace(let, "0", 1)
        if copy.find(let) != -1:
            if let in high.keys():
                if high[let] >= copy.find(let) - txt.find(let):
                    continue
                else:
                    high[let] = copy.find(let) - txt.find(let)
            else:
                high[let] = copy.find(let) - txt.find(let)
​
            txt = txt.replace(let, "1", 1)
    max_value_keys = [key for key in high.keys() if high[key] == max(high.values())]
    return sorted(max_value_keys)

