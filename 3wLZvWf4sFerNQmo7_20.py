
def neutralise(s1, s2):
  new_string=""
  for i in range (len(s1)):
    if s1[i]==s2[i]:
      new_string=new_string+s1[i]
    else:
      new_string=new_string+"0"
  return new_string

