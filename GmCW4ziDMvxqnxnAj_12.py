
def check(val_con):
  s=[]
  for char in val_con:
    s=char.split('/')
    if int(s[0]) / int(s[1]) != 1 :
      return False
  return True
def who_passed(students):
  result=[]
  for key in students:
    c= check(students[key])
    if c is True :
      result.append(key)
  result.sort()   
  return result

