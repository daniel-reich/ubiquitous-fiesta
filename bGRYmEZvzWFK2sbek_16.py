
def get_missing_letters(s):
  k = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']   
  k1 = list(s)
  k2 = ""
  l = []
  for i in k :
    if i not in k1 :
      l.append(i)
  for i in l :
    k2 = k2 + i
  return k2

