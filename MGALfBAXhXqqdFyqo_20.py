
a = [chr(i) for i in range(ord('a'),ord('z')+1)]
b = [chr(i) for i in range(ord('A'),ord('Z')+1)]
​
def atbash(txt):
    g = []
    for z in txt:
        if z.isupper() == True:
            g.append(chr(65+(abs(ord(chr(90-ord(z)))))))
        if z.islower() == True:
            g.append(chr(97 + (abs(ord(chr(122 - ord(z)))))))
        elif not z.isalpha() == True:
            g.append(z)
    return("".join(g))

