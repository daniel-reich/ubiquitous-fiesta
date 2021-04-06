
def determine_who_cursed_the_most(d):
  m = sum([d[i]['me'] for i in d])
  s = sum([d[i]['spouse'] for i in d])
  return 'ME!' if m>s else 'SPOUSE!' if s>m else 'DRAW!'

