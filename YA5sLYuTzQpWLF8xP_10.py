
def clean_up_list(lst):
  even=[]
  odd=[]
  for x in lst:
    if int(x)%2:
      odd.append(int(x))
    else:
      even.append(int(x))
  return [even,odd]

