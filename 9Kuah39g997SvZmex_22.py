
def common_last_vowel(txt):
    v=["a","e","o","i","u"]
    w=[word for word in txt.lower().split()]
    lst = []
    for word in w:
        lst.append([char for char in word if char in v][-1])
        
    d ={lst.count(item):item for item in lst}
    max_v = max(d.keys())
    
    return d[max_v]

