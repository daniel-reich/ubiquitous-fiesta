
def delete_occurrences(lst, num):
  lst1=[]
  for i in lst:
    y=lst1.count(i)
    if y<num:
       lst1.append(i)    
  return lst1

