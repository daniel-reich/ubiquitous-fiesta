
def greatest_impact(lst):
  lst = [[i[j]*3 if j in [0,1,3] else i[j]*10 for j in range(4)] for i in lst]
  diff = [sum([abs(j[0]-j[i]) for j in lst])/len(lst) for i in [1,2,3]]
  if len(set(diff))==1:
    return 'Nothing'
  if diff[0]==min(diff):
    return 'Weather'
  elif diff[1]==min(diff):
    return 'Meals'
  else:
    return 'Sleep'

