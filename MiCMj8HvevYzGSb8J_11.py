
def start(n):
      return n > 1 and start(n-1) + start(n-2) or n == 1 and start(n-1) + 'b' or 'a'
​
def fibo_word(n):
    return n < 2 and 'invalid' or 'b, '+', '.join([start(k-2) for k in range(2, n+1)])

