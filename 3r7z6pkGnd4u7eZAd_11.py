
def mark_maths(lst):
  count = 0
  t = ','.join(lst).replace('=','==')
  for item in lst:
    if eval(item.replace('=','==')):
      count += 1
  return str(round(count/len(lst)*100)) + '%'

