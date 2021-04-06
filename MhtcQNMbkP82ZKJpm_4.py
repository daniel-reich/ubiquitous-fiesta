
def get_notes_distribution(students):
  A=[]
  for x in students:
    A+=x['notes']
  D={}
  for i in [1,2,3,4,5]:
    if A.count(i)>0:
      D[i]=A.count(i)
  return D

