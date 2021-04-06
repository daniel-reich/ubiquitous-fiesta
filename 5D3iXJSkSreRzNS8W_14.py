
def news_at_ten(txt, n):
  return [''.join([' ' for a in range(n - i)]) + ''.join([txt[b:b + 1] for b in range(i-n if i-n>0 else 0, i)]) +''.join([' ' for b in range(i - len(txt))]) for i in range(n + len(txt) + 1)]

