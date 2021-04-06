
def dance(lst,parameter):
  def gender_seperator(lst):
    men = []
    women = []
    
    for item in lst:
      women.append(item[0])
      men.append(item[1])
    
    return [women, men]
  def position_reverser(lst):
    return list(reversed(lst))
  
  dancers_by_gender = gender_seperator(lst)
  
  women = dancers_by_gender[0]
  men = dancers_by_gender[1]
  
  if parameter == 'women':
    women = position_reverser(women)
  elif parameter == 'men':
    men = position_reverser(men)
  
  return [list(i) for i in zip(women, men)]

