
def shared_letters(a, b):
  c=""
  for x in a.lower():
    if x in b.lower():
      if x not in c:
        c+=x
  c=sorted(c)
  return "".join(c)

