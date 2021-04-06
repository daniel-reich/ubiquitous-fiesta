
def isbn13(txt):
  if not (len(txt)==10 or len(txt)==13):
    return "Invalid"
  elif len(txt)==13:
    total=0
    i=1
    for t in txt:
      total+=int(t)*i
      if i==1:
        i=3
      else:
        i=1
    if total%10==0:
      return "Valid"
    else:
      return "Invalid"
  else:
    total=0
    j=10
    isbn13="978"
    for t in txt:
      if t=='X':
        total+=10
      else:
        total+=int(t)*j
        j-=1
    if total%11==0:
      isbn13+=str(txt)[:-1]
      total=0
      i=1
      for t in isbn13:
        total+=int(t)*i
        if i==1:
          i=3
        else:
          i=1
      if total%10==0:
        isbn13+="0"
        return isbn13
      else:
        isbn13+=str(10-total%10)
        return isbn13
    else:
      return "Invalid"

