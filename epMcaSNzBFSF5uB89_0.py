
def currently_winning(s):
  home = [sum(s[0:i:2]) for i in range(1,len(s),2)]
  away = [sum(s[1:i:2]) for i in range(2,len(s)+1,2)]
  return ["O" if h<a else "T" if h==a else "Y" for h,a in zip(home,away)]

