
def super_reduced_string(txt):
  lst = ["$"]
  for i in txt:
    if lst[-1] == i:
      lst.pop()
    else:
      lst.append(i)
  
  lst.remove("$")
  if len(lst)>0:
    string = ''.join([elem for elem in lst]) 
  else:
    string = 'Empty String'
  return string

