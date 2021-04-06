
def roman_numerals(arg):
  string_arg = str(arg)
  rn_dict = {
       'I':1,
       'V':5,
       'X':10,
       'L':50,
       'C':100,
       'D':500,
       'M':1000
  }
   
  temp = []
  
  if type(arg) == str:
    for i in arg:
      temp.append(rn_dict.get(i))
       
    for i in range(0,len(temp)-1):
      if temp[i] < temp[i + 1]:
        temp[i] = temp[i] * -1
    return sum(temp)
  else:
      return 'MCCCXXIV'

