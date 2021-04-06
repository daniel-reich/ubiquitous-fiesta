
def special_reverse(s, c):
  x=""
  b=s.split()
  for i in b:
    if i[0]==c:
       x+= i[::-1] +" "
    else:
      x+=i +" "
  return x[:-1]
print(special_reverse("peter piper picked pickled peppers", "p"))

