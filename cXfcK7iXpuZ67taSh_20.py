
def mystery_func(txt):
  return "".join(int(txt[i])*txt[i-1]for i in range(len(txt)) if i%2)

