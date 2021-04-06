
def overlap(s1, s2):
  smaller = min([len(s1),len(s2)])
  if s1 == s2:
    return s1
  if s1 in s2: 
    return s2
  for i in range(smaller): 
    backthrough = smaller - i - 1
    revthrough = (-1 * backthrough)
    print(backthrough)
    print(revthrough)
    print(s1[revthrough:])
    print(s2[0:backthrough])
    print('-----')
    if s1[revthrough:] == s2[0:backthrough]: 
      begin = s1[0:revthrough]
      end = s2[backthrough:]
      overlap = s1[revthrough:]
      return begin + overlap + end
  return s1+s2

