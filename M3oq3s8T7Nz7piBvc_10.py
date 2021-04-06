
def even_odd_string(txt):
  even = "".join(char for i,char in enumerate(txt) if i%2==0)
  odd =  "".join(txt[i] for i in range(len(txt)) if i%2)
  return even+" "+odd

