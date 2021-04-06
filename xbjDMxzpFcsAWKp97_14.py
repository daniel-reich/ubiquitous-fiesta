
def can_see_stage(seats):
​
  for col in range(len(seats[0])):
    list_=[row[col] for row in seats]
​
    if sorted(list_)!=list_:
      return False
    if len(set(list_))!=len(list_):
      return False
    
  return True

