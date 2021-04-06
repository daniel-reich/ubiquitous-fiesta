
def news_at_ten(txt: str, n: int) -> list:
  txt = ' ' * n + txt + ' ' * n
  return [txt[i : i + n] for i in range(len(txt) - n + 1)]

