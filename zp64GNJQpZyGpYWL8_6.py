
def score_it(s):
  t = 0
  nl = 0
  ns = ''
  for c in s:
    if(c == '('):
      if(ns != ''):
        t += int(ns) * nl
        ns = ''
      nl += 1
    elif(c == ')'):
      if(ns != ''):
          t += int(ns) * nl
          ns = ''
      nl -= 1
    elif(ord(c) >= 48 and ord(c) <= 57):
      ns += c
  return t

