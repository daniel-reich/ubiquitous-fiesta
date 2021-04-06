
def camel_to_snake(s):
  output = ""
  for i in range(0,len(s)-1): 
    if s[i+1].isupper():
      output+=s[i]+'_'
      i+=2
    else:
      if s[i].islower():
        output+=s[i]
      else:
        output+=s[i].lower()
  
  return output+s[-1]

