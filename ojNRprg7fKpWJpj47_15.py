
def shift_sentence(txt):
  string = "" 
  txt = txt.split() 
  last = txt[-1][0]
  string += txt[0].replace(txt[0][0], txt[-1][0], 1) + ' '
  for i in range(len(txt) - 1):
    string += txt[i+1].replace(txt[i+1][0], txt[i][0], 1) + " "
​
  
  
  
  return string.rstrip()

