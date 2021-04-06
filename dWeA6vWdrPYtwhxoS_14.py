
def count_number(lst):
  count = 0
  lst = ''.join(''.join(str(lst).split('[')).split(']')).split(', ')
  for x in lst:
    try:
      float(x)
      count += 1
    except: pass
  return count

