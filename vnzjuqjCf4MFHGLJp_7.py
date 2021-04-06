
def shift_letters(txt, n):
​
    result = [a for a in txt.split(' ')]
    result_n = ''.join([a for a in txt.split(' ')])
​
    for a in range(n):
        result_n = result_n[-1] + result_n[0:(len(result_n)-1)]
​
    result_n = list(result_n)
​
    for a in range(len(txt)):
       if txt[a] == ' ':
           result_n.insert(a, ' ')
​
    return ''.join([a for a in result_n])

