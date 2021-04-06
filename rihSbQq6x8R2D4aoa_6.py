
def alpha_range(start, stop, step = 1):
  
  alph_low = 'abcdefghijklmnopqrstuvwxyz'
  alph_upp = 'abcdefghijklmnopqrstuvwxyz'.upper()
  nums = range(1, 27)
  
  alph_nums_low = {}
  alph_nums_high = {}
  nums_alph_low = {}
  nums_alph_high = {}
  
  for n in nums:
    alph_nums_low[alph_low[n-1]] = n
    alph_nums_high[alph_upp[n-1]] = n
    nums_alph_low[n] = alph_low[n-1]
    nums_alph_high[n] = alph_upp[n-1]
  
  start_case = 'L' if start.islower() == True else 'U'
  stop_case = 'L' if stop.islower() == True else 'U'
  
  if start_case != stop_case:
    return 'both start and stop must share the same case'
    
  elif start_case == 'L':
    
    start = alph_nums_low[start]
    stop = alph_nums_low[stop]
    if step > 0:
      start, stop = sorted([start, stop])
    else:
      start, stop = list(reversed(sorted([start, stop])))
      
    if step in range(-26, 27) and step != 0:
      if step > 0:
        return [nums_alph_low[n] for n in range(start, stop + 1, step)]
      else:
        return [nums_alph_low[n] for n in range(start, stop - 1, step)]
    else:
      return 'step must be a non-zero value between -26 and 26, exclusive'
  
  else:
    
    start = alph_nums_high[start]
    stop = alph_nums_high[stop]
    
    if step > 0:
      start, stop = sorted([start, stop])
    else:
      start, stop = list(reversed(sorted([start, stop])))
    
    if step in range(-26, 27) and step != 0:
      if step > 0:
        return [nums_alph_high[n] for n in range(start, stop + 1, step)]
      else:
        return [nums_alph_high[n] for n in range(start, stop - 1, step)]
    else:
      return 'step must be a non-zero value between -26 and 26, exclusive'

