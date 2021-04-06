
def min_swaps(string):
  cnt=0
  dig='0'
  for x in string:
    if dig!=x: cnt+=1
    dig='1' if dig=='0' else '0'
  if cnt<len(string)-cnt: return cnt
  else: return len(string)-cnt

