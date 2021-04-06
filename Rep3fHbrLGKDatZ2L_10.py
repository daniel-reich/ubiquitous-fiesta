
def complete_pattern(s):
    index = s.find("_")
    for item in set(s) - {'_'}:
        complete_string = s.replace("_", item)
        for k in range(1, len(s)//2+1):
            if all(complete_string[i:i+k] == complete_string[0:k] for i in range(0, len(s), k) if i + k <= len(s)):
                if k-1 >= index:
                    return item
                else:
                    return s[index % k]

