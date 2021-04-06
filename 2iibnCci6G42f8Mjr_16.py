
def guess_score(code, guess):
    d={"black":0,"white":0}
    for i in range(len(code)):
        if(code[i]==guess[i]):
            d['black']+=1
        if(code[i]!=guess[i] and code[i] in guess):
            d['white']+=1       
    return d

