
def upper_index(txt):
  array=[]
  for x in range(0,len(txt)):
    if txt[x].isupper()==True:
      array.append(1)
    else:
      array.append(0)
  return array
​
def convert_text(txt, array):
  new_txt= txt.lower()
  result=''
  for x in range(0,len(array)):
    if array[x]==0:
      result= result + new_txt[x]
    else:
      result= result + new_txt[x].upper()
  return result
​
def space_index(txt):
  array=[]
  for x in range(0,len(txt)):
    if txt[x]==' ':
      array.append(1)
    else:
      array.append(0)
  return array
​
def remove_spaces(txt):
  string=''
  for x in range(0,len(txt)):
    if txt[x]!=' ':
      string= string + txt[x]
  return string
  
def new_spaces(txt, array):
  string=remove_spaces(txt)
  new_string=''
  spaces=0
  for x in range(0, len(string)):
    y=x+spaces
    if array[y]==0:
      new_string += string[x]
    elif array[y]!=0:
      new_string +=' '+string[x]
      spaces+=1
      x=x-1
  return new_string
​
def special_reverse_string(txt):
  index_array=upper_index(txt)
  index_space=space_index(txt)
  result=new_spaces(txt[::-1], index_space)
  return convert_text(result, index_array)

