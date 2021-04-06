
def add_letters(a):
  ans=sum(ord(x)-96 for x in a)%26+96
  if ans==96:
    return "z"
  return chr(ans)

