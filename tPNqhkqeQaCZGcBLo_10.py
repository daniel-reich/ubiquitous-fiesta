
def determine_who_cursed_the_most(d):
  m,s = 0,0
  for i in d:
    m+=d[i]['me']
    s+=d[i]['spouse']
  return 'DRAW!' if m==s else 'ME!' if m>s else 'SPOUSE!'

