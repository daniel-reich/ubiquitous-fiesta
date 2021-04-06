
def markdown(symb):
  def format_txt(txt, s):
    ans = ''
    for x in txt.split():
      if x.lower().find(s.lower()) != -1:
        x = symb + x + symb
      ans += x + ' '
    return ans[:-1]
  return format_txt

