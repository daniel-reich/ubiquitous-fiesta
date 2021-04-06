
def get_primiera_score(deck):
    b = {'d','c','s','h'}
    v = {'A':16,'7':21,'6':18,'2':12,'3':13,'4':14,'5':15,'J':10,'Q':10,'K':10}
    ans = {'d':0,'h':0,'c':0,'s':0}
    c = {i[-1] for i in deck}
    if b != c: return 0
    for i in deck:
        if ans[i[-1]] < v[i[:-1]]: ans[i[-1]] = v[i[:-1]]
    return sum(ans.values())
​
print(get_primiera_score(["2d", "Jd", "Qc", "5s", "As"]))

