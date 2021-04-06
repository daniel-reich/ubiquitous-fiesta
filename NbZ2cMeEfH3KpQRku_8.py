
def portion_happy(b):
  h = sum([b[0]==b[1]]+[b[i-1]==b[i] or b[i]==b[i+1] for i in range(1,len(b)-1)]+[b[-2]==b[-1]])
  return h/len(b)

