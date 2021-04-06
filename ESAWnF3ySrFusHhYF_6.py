
def edit_words(lst):
    return [f(w) for w in lst]
​
def f(x):
    x = x[::-1].upper()
    ln = len(x) // 2
    if len(x) % 2 == 0:
        x = x[:ln] + '-' + x[ln:]
    else:
        x = x[:ln+1] + '-' + x[ln+1:]
    return x

