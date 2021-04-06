
def delete_occurrences(y,n):
  j=[]
  [j.append(i) for i in y if j.count(i)<n]
  return j

