
def fibo_word(n):
    if n < 3:
        return 'invalid'
    else:
        lst = ['b', 'a']
        for i in range(2, n):
            lst.append(lst[i-1]+lst[i-2])
    return ', '.join(lst)

