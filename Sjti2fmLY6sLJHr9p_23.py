
def look_and_say(start, n):
    result = [start]
    for y in range(n-1):
        # step 1: substing
        substrings = []
        if len(str(result[-1])) == 1:
            substrings.append(str(result[-1]))
        else:
            sub = str(result[-1])[0]
            for i in range(0,len(str(result[-1]))):
                if i != 0:
                    if str(result[-1])[i] in sub:
                        sub += str(result[-1])[i]
                    else:
                        substrings.append(sub)
                        sub = str(result[-1])[i]
            substrings.append(sub)
        # step 2: count + turn into digits
        result.append(int("".join([str(len(i))+i[0] for i in substrings])))
    return result

