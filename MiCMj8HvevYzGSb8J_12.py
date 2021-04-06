
def fibo_word(n):
    if n<2:
        return "invalid"
    else:
        lst = ['b', 'a']
        for iter in range(2, n):
            lst.append(lst[iter-1]+lst[iter-2])
    return ', '.join(lst)

