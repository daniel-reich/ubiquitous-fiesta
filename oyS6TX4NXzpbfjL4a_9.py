
def best_start(lst, word):
    scores=dict(zip(list("abcdefghijklmnopqrstuvwxyz"),[1,3,3,2,1,4,2,4,1,8,5,2,3,1,1,3,10,1,1,1,1,4,4,8,4,10]))
    mults=dict(zip(["-","DW","DL","TL"],[1,1,2,3]))
    index=0
    best_score=0
    for i in range(len(lst)-len(word)+1):
        score=sum([mults[lst[i+n]]*scores[word[n]] for n in range(len(word))])
        if "DW" in lst[i:i+len(word)]: score*=2
        if score>best_score: 
            index=i
            best_score=score
    return index

