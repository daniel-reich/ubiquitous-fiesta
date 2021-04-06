
def score_calculator(easy, med, hard):
    k=[]
    if easy<0 or med<0 or hard<0:
        return 'invalid'
    for i in easy*5,med*10,hard*20:
        k.append(i) 
    return sum(k)

