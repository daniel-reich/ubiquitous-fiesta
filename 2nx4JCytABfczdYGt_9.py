
di = {
1:  ["Io ", "o"], 
2:  ["Tu ", "i"], 
3:  ["Egli ", "a"], 
4:  ["Noi ", "iamo"], 
5:  ["Voi ", "ate"], 
6:  ["Essi ", "ano"]}
​
def conjugate(verb, pronoun):
  root = verb[:-3]
  if root[-1] in "cg":
    if pronoun in [2,4]:
      root += "h"
  if root[-1] == "i":
    if pronoun in [2,4]:
      root = root[:-1]
  return di[pronoun][0]+root+di[pronoun][1]

