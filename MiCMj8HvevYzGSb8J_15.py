
def fibo_word(n):
    if n < 2:
        return 'invalid'
    arr = ['b', 'a']
    for _ in range(2, n):
        arr.append(arr[-1] + arr[-2])
    return ', '.join(arr)

