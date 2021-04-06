
def three_letter_collection(s):
    res = []
    for i in range(len(s)-2):
        res.append(s[i:i+3])
    return sorted(res)

