
def cap_space(txt):
 result = ""
 for i in txt:
  if i.isupper():
   result += " " + i
  else:
   result += i
 return result.lower()

