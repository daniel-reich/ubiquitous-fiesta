
def encryption(txt):
    txt = txt.replace(' ','')
    answer = ''
    for i in range(int(len(txt)**0.5)+1):
        answer = answer + txt[i::round(len(txt)**0.5+.5)] + ' '
    return answer[:-1]

