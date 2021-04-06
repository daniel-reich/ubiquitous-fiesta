
def calculate_scores(txt):
  An=0
  Be=0
  Ch=0
  for i in txt:
    if i=='A':
      An+=1
    elif i=='B':
      Be+=1
    elif i=='C':
      Ch+=1
  return [An,Be,Ch]

