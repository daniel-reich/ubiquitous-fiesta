
def clean_up_list(lst):
  even=[]
  odd=[]
  for i in lst:
    i=int(i)
    if int(i)%2==0 :
      even=even+[i]
    else:
      odd=odd+[i]
    output=[even,odd]
  return output

