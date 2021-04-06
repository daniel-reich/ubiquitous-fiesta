
def secret(txt):
    level1 = txt.split('>')[0]
    txt = ''.join(txt.split('>')[1:])
    level2 = txt.split('.')[0]
    txt = ''.join(txt.split('.')[1:])
    base = txt.split('$')[0]
    n = txt.count('$')
    classes = int(txt.split('*')[1])
    ans = "<" + level1 + ">"
    for i in range(1, classes + 1):
        ans += "<" + level2 + " class='" + base + str(i).zfill(n) + "'></" + level2 + ">"
    ans += "</" + level1 + ">"
    return ans

