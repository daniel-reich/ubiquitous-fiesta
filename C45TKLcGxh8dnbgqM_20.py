
def caesar_cipher(s, k):
  alpha="abcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyz"
  cipher=""
  cycle=k-((k//26)*26)
  for i in s:
    if i.isalpha():
      if i.isupper():
        ind=int(alpha.index(i.lower()))
        ind+=cycle
        cipher+=alpha[ind].upper()
      else:
        ind=int(alpha.index(i))
        ind+=cycle
        cipher+=alpha[ind].lower()
    else:
      cipher+=i
​
  return cipher

