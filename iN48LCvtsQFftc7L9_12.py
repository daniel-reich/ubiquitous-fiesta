
def word_search(letters, words):
    out = []
    word_list = []
    for  i in range(0,len(letters),8):
        word_list.append(list(letters[i:i+8]))
    for m in range(len(word_list)):
        h = ''; v = '';
        for n in range(len(word_list)):
            d1 = ''; d2 = ''; d3 = ''; d4 = ''
            h += word_list[m][n]
            v += word_list[n][m]
            a = m
            b = n
            c = m
            d = n
            while a < len(word_list) and b<len(word_list):
                d1 += word_list[a][b]
                a += 1
                b += 1
            out.append(d1)
            while c < len(word_list) and d>=0:
                d2 += word_list[c][d]
                c += 1
                d -= 1
            out.append(d2)
            e = m; f = n
            while e >=0 and f>= 0:
                d3 += word_list[e][f]
                print(d3)
                e -= 1
                f -=1
            out.append(d3)
            g = m;o = n
            while g>= 0 and o<len(word_list):
                d4 += word_list[g][o]
                g -= 1
                o += 1
            out.append(d4)
        out.append(h)
        out.append(v)
    t = []
    for w in words:
        for word in out:
            if w in word.lower() or w[::-1] in word.lower():
                t.append(w)
    if len(set(t)) == len(words):
        return True
    return False

