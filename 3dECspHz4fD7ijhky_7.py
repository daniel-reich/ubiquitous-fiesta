
class Sequence:
​
  def __init__(self, start, end):
​
    self.start = start
    self.end = end
​
    self.seq = list(range(start, end + 1))
  
  def match(self, start, lst):
​
    sindex = lst.index(start)
​
    start_seq = self.seq[self.seq.index(start):]
​
    match = []
    n = 0
​
    try:
      while lst[sindex + n] == start_seq[n]:
        match.append(start_seq[n])
        n += 1
    except IndexError:
      pass
​
    if len(match) >= 3:
      return ['{}-{}'.format(min(match), max(match)), match]
    else:
      return str(start)
​
​
def numbers_range(numbers):
​
  if len(numbers) <= 0:
    return ''
    
  seq = Sequence(min(numbers), max(numbers))
​
  matches = []
  used = []
​
  for n in range(len(numbers)):
    number = numbers[n]
    if number in used:
      pass
    else:
      matched = seq.match(number, numbers)
      if isinstance(matched, list) == False:
        matches.append(matched)
      else:
        matches.append(matched[0])
        for item in matched[1]:
          used.append(item)
  
  return ', '.join(matches)

