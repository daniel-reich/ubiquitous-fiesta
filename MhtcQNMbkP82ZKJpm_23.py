
def get_notes_distribution(students):
  dict1={}
  lst=[]
  for i in students:
      lst.extend(i['notes'])
  for i in lst:
      if i in [1,2,3,4,5]:
          dict1.update({i:lst.count(i)})
  return dict1

