
def three_letter_collection(s):
  if len(s) <3:
    return []
  else:
    sort=[]
    i=0
    while i< len(s)+1:
      if i+2 == len(s): 
        break
      else:
        x=s[i:i+3]
        sort.append(x)
        i+=1
    return sorted(sort)

