
def happiness_number(s):
  a = 0
  b = 2
  suma = 0
  for i in range(len(s)-1):
    if ':)' == s[a:b]:
      suma +=1
    elif ':('  == s[a:b]:
      suma -= 1
    elif '(:'  == s[a:b]:
      suma += 1
    elif '):'  == s[a:b]:
      suma -= 1
    a += 1
    b += 1
  return suma

