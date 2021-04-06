
def news_at_ten(txt, n):
  scrolltxt = (" " * n) + txt + (" " * n)
  return [scrolltxt[i:n + i] for i in range(len(scrolltxt) - (n - 1))]

