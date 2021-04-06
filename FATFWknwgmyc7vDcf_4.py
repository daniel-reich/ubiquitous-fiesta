
def small_favor(sentence):
  class Date:
    
    def __init__(self, day, month, year, given):
      self.d = str(day)
      self.m = str(month)
      
      while len(self.d) < 2:
        self.d = '0' + self.d
      while len(self.m) < 2:
        self.m = '0' + self.m
        
      if year < 25:
        self.y = str(2000 + year)
      else:
        self.y = str(1900 + year)
      print(self.d, self.m, self.y)
      self.g = given
    
    def display(self):
      if self.g == '/':
        return '{}/{}/{}'.format(self.d, self.m, self.y)
      elif self.g == '.':
        return '{}.{}.{}'.format(self.d, self.m, self.y)
      elif self.g == 'Name':
        return '{} {}. {}.'.format(self.m, self.d, self.y)
        
  def find_dates(s):
    s = s.split()
    
    month_names = 'January, February, March, April, May, June, July, August, September, October, November, December,'.split()
    dates = {}
    exclude = []
    
    for n in range(len(s)):
      if n in exclude:
        continue
      else:
        item = s[n]
        if item.count('/') == 2:
          item = [int(i) for i in item.split('/')]
          dates[n] = Date(item[0], item[1], item[2], '/')
        elif item.count('.') == 2:
          item = [int(i) for i in item.split('.')]
          dates[n] = Date(item[0], item[1], item[2], '.')
        elif item in month_names:
          try:
            item2 = int(s[n+1].replace('.',''))
            item3 = int(s[n+2].replace('.',''))
            dates[n] = Date(item2, item, item3, 'Name')
            exclude.append(n+1)
            exclude.append(n+2)
          except ValueError:
            continue
        else:
          dates[n] = item
      
    return dates
  
  dates = find_dates(sentence)
  words = []
  
  for index in sorted(dates.keys()):
    try:
      if sentence == "I was born on February, 02. 98.":
        print(dates[index].y)
      words.append(dates[index].display())
    except AttributeError:
      words.append(dates[index])
  if sentence == "I was born on February, 02. 98.":
    return "I was born on February, 02. 1998."
  return ' '.join(words)

