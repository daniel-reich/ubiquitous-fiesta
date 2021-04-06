
MONTH = ["January", "February", "March", "April", "May", "June", "July",
         "August", "September", "October", "November", "December"]
​
def case1(sentence, sep, month, pos):
    if pos < 2 or pos > len(sentence) - 2:
        return sentence
    chunk = sentence[pos-2:pos+4+2]
    try:
        day = int(chunk[:2])
        year = int(chunk[-2:])
        year = 2000 + year if year < 24 else 1900 + year
        return sentence[:pos+4] + str(year) + sentence[pos+6:]
    except:
        return sentence
​
def case2(sentence, month, pos):
    chunk = sentence[pos+len(month):pos+len(month)+9]
    if chunk[:2] != ", " or chunk[4] != "." or chunk[-1] != ".":
        return sentence
    try:
        day = int(chunk[2:4])
        year = int(chunk[6:8])
        year = 2000 + year if year < 24 else 1900 + year
        return sentence[:pos] + month + chunk[:-3] + str(year) + "." + sentence[pos+len(month)+9:]
    except:
        return sentence
​
def small_favor(sentence):
    for month in MONTH:
        positions = [k for k in range(len(sentence)-len(month)) if sentence[k:k+len(month)] == month]
        for pos in positions:
            sentence = case2(sentence, month, pos)
    for sep in ['.', '/']:
        for m in range(1, 13):
            month = str(m).zfill(2)
            a = sep + month + sep
            positions = [k for k in range(len(sentence)-4) if sentence[k:k+4] == a]
            for pos in positions:
                sentence = case1(sentence, sep, month, pos)
    return sentence

