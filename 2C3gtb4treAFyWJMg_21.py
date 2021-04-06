
def splitbytwo(txt):
    return [txt[2*i:2*i+2] for i in range(int(len(txt)/2))]
​
def polybius(text):
    letters = [chr(i) for i in range(97,123) if i != 106]
    numbers = [str(10*a+b) for a in range(1,6) for b in range(1,6)]
    LtoN = dict(zip(letters,numbers))
    LtoN[' '] = ' '
    LtoN['j'] = '24'
    NtoL = dict(zip(numbers,letters))
    NtoL[' '] = ' '
    if text.replace(' ','').isdigit():
        return ' '.join([''.join([NtoL[s] for s in lst]) for lst in map(splitbytwo,text.split())])  
    else:
        return ' '.join([''.join([LtoN[c] for c in word if c in LtoN.keys()]) for word in text.lower().split()])

