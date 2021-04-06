
def sun_loungers(beach):
  if beach == '0':
    return 1
  adjusted = list(beach)
  if beach.startswith('00'):
    adjusted[0] = '1'
  if beach.endswith('00'):
    adjusted[-1] = '1'
  for place, lounge in enumerate(adjusted[1:-1], start=1):
    if (lounge == '0'
      and adjusted[place - 1] == '0'
      and adjusted[place + 1] == '0'):
      adjusted[place] = '1'
  return adjusted.count('1') - beach.count('1')

