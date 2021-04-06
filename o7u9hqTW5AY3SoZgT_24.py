
def switcheroo(txt):
    return ' '.join([f(word) for word in txt.split()])
​
def f(w):
    x = w.rfind('nts')
    y = w.rfind('nce')
    if x == y == -1:
        return w
    if x > y:
        return plug(w, x, 'nce')
    else:
        return plug(w, y, 'nts')
​
def plug(w, i, s):
    for v in w[i+3:]:
        if v.isalpha():
            return w
    return w[:i] + s + w[i+3:]

