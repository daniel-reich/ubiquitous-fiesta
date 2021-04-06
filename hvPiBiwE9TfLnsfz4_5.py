
def generate_word(n):
​
    def let_fib(seq1, seq2, num):
        if num == 0:
            return []
        lst = [seq1+seq2]
        lst.extend(let_fib(seq2, seq1+seq2, num-1))
        return lst
​
    if n < 2:
        return 'invalid'
    elif n == 2:
        return 'b, a'
    lst = ['b', 'a']
    lst.extend(let_fib('b', 'a', n-2))
    return ', '.join(lst)

