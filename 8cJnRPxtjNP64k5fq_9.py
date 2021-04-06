
def dance(lst,parameter):
  women = []
  men = []
  final_list =[]
  for i in range(len(lst)):
    women.append(lst[i][0])
    men.append(lst[i][1])
  
  if parameter == 'men':
    for i, j in zip(men[::-1],women):
      final_list.append([j,i])
​
  if parameter == 'women':
    for i, j in zip(men,women[::-1]):
      final_list.append([j,i])
  
  return final_list

