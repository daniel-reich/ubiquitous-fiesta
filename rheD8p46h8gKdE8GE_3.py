
def check_array(array):
  new_array=[]
  for x in range(0,3):
    if array[x]>255:
      new_array.append(255)
    elif array[x]<0:
      new_array.append(0)
    else:
      new_array.append(array[x])
  return new_array
  
def convert_to_gray(array):
  liste=[]
  if sum(array)<=0:
    return [0,0,0]
  elif sum(array)>=765:
    return [255,255,255]
  else:
    result=round(sum(array)/3)
  for x in range(0,3):
    liste.append(result)
  #print(liste)
  return liste
​
def grayscale(lst):
  full_list=[]
  sub_list=[]
  for x in range(0, len(lst)):
    for y in range(0, len(lst[0])):
      array = check_array(lst[x][y])
      sub_list.append(convert_to_gray(array))
    full_list.append(sub_list)
    sub_list=[]
  return full_list

