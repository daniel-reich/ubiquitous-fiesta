
def possible_palindrome(txt):
  x=txt
  o=0
  v=0
  def count_string(x,a):
    count=0
    for i in x:
      if i==a:
        count+=1
    return count
  for i in range(len(x)):
    o = count_string(x,x[i])
    if o % 2 == 1:
      v+=1
  if v<=1 or x[0]==x[1]==x[2]:
    return(True)
  else:
    return(False)

