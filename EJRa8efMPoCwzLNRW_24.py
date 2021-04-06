
def dakiti(sentence):
    import re
    pattern = '\d+'
    resu = re.findall(pattern, sentence)
    result = re.split(pattern, sentence) 
    res = ''.join(result)
    res = res.split(' ')
    new = []
    print(resu)
    print(res)
    for i in range(0,len(res)):
        if str(i + 1) in resu:
            new.append(res[resu.index(str(i + 1))])
    return ' '.join(new)

