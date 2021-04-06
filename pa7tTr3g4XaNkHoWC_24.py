
def pig_latin_sentence(txt: str) -> str:
    vowels = {'a', 'e', 'i', 'o', 'u'}
    ans = []
    for i in txt.split():
        if i[0] in vowels:
            ans.append(i + 'way')
        else:
            k = 0
            for j in i:
                if j in vowels:
                    break
                k += 1
            ans.append(i[k:] + i[:k] + 'ay')
    return ' '.join(ans)

