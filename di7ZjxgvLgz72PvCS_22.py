
def validate_swaps(lst,words):
    e = []
    for word in lst:
        if len(word) != len(words):
            e.append(False)
        else:
            a = ''
            b = ''
            for i in range(len(word)):
                if word[i] != words[i]:
                    a += word[i]
                    b += words[i]
            if a == b[::-1]:
                e.append(True)
            else:
                e.append(False)
    return e

