
def greatest_impact(lst):
  if all(row[0]==10 for row in lst):
    return 'Nothing'
    
  factors =  [{'name':'Weather', 'weighted':lambda v:10-v, 'impact':0},
        {'name':'Meals', 'weighted':lambda v:3-v, 'impact':0},
        {'name':'Sleep', 'weighted':lambda v:10-v, 'impact':0}]
  for mood, *row in lst:
    for i, value in enumerate(row):
      factors[i]['impact'] += factors[i]['weighted'](value)
  return max(factors,key=lambda x: x['impact']/len(lst))['name']

