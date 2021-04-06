
def numbers_range(ranges):
  ranges.sort()
  if not ranges: return ""
  
  ans = []
  lo = hi = ranges[0]
  for n in ranges[1:]:
    if n==hi+1:
      hi+=1
    else:
      if hi-lo>1:
        ans.append('{}-{}'.format(lo,hi))
      elif lo==hi:
        ans.append(str(hi))
      else:
        ans.append(str(lo))
        ans.append(str(hi))
      lo=hi=n
  if hi-lo>1:
    ans.append('{}-{}'.format(lo,hi))
  elif lo==hi:
    ans.append(str(hi))
  else:
    ans.append(str(lo))
    ans.append(str(hi))
  return ', '.join(ans)

