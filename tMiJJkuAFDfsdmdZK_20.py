
def to_snake_case(txt):
  S = ""
  for i in txt:
    if i.isupper():
      S += "_"+i.lower()
    else:
      S+=i
  return S
​
def to_camel_case(txt):
  T = txt.split("_")
  if len(T)>1:
    return T[0]+"".join(T[i].capitalize() for i in range(1,len(T)))
  return txt

