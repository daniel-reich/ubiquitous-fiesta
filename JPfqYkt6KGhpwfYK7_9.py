
def replace_the(txt):
    low = txt.split()
    return ' '.join([f(i, low) for i in range(len(low))])
​
def f(i, low):
    if low[i] == 'the':
        if low[i+1][0] in 'aeiou':
            return 'an'
        else:
            return 'a'
    return low[i]

