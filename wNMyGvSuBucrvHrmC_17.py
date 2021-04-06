
class Substring:
  
  def __init__(self, substring):
    self.s = substring
  
  def repeat(self, times):
    return self.s * times
  
  def match(self, string):
    test_string = self.s
    times = 2
    while len(test_string) < len(string):
      test_string = self.repeat(times)
      times += 1
    if len(test_string) == len(string):
      if test_string == string:
        return times-1
      else:
        return False
    else:
      return False
  
  def __str__(self):
    return self.s
​
def number_of_repeats(s):
  
  substrings = []
  half_index = len(s) // 2 + 1
  
  for n in range(half_index):
    substrings.append(Substring(s[:n+1]))
  
  for substring in substrings:
    if substring.match(s) != False:
      return substring.match(s)
  
  return 1

