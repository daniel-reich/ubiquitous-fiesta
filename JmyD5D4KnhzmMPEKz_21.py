
def constraint(txt):
    txt = txt.lower()
    words, letters = txt.split(), ''.join(i for i in txt if i.isalpha())
​
    pan = len(set(letters)) == 26
    het = len(set(letters)) == len(letters)
    tau = len(set([i[0] for i in words])) == 1
    tran = len(set.intersection(*[set(i) for i in words]))
​
    return 'Pangram' if pan else 'Heterogram' if het else 'Tautogram' \
        if tau else 'Transgram' if tran else 'Sentence'

