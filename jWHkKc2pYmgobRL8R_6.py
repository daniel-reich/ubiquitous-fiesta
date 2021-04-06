
def distance_to_nearest_vowel(txt):
    vowels = 'aeiou'
    res = []
    for idx, char in enumerate(txt):
        if char in vowels:
            res.append(0)
        else:
            forward = backward = 1000
            for x in range(1, len(txt) - idx):
                if txt[idx + x] in vowels:
                    forward = x
                    break
            for y in range(0, idx + 1 ):
                if txt[idx - y] in vowels:
                    backward = y
                    break
            if forward < backward:
                res.append(forward)
            else:
                res.append(backward)
    return res

