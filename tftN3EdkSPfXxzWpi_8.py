
txt = "I have a dog. I have a log. There is no stopping me now."
n = -1
def sentence_searcher(txt, n):
    txt = txt.split(' ')
    pIn = [0]
    for i in range(len(txt)):
        if '.' in txt[i]:
            pIn.append(i)
    nrange = []
    for i in range(1,len(pIn)):
        if n>=0 and pIn[i-1]<=n<=pIn[i]:
            nrange.append(pIn[i-1])
            nrange.append(pIn[i])
        if n<0 and pIn[i-1]<=len(txt)+n<=pIn[i]:
            nrange.append(pIn[i-1])
            nrange.append(pIn[i])
    if 0 in nrange:
        s = ''
        for i in txt[nrange[0]:nrange[1]+1]:
            s=s+' '+i
        return s.strip()
    elif 0 not in nrange:
        s = ''
        for i in txt[nrange[0]+1:nrange[1]+1]:
            s=s+' '+i
        return s.strip()
sentence_searcher(txt, n)

