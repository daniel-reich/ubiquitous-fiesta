
def is_smooth(sentence):
  a=[]
  for word in sentence.split(" "):
    a.append(word[0])
    a.append(word[-1])
  b=a[1:-1]
  return all(b[i].lower()==b[i+1].lower() for i in range(0,len(b),2))

