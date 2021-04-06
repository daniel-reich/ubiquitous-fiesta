
def look_and_say(n):
  
  s = str(n)
  even = len(s)%2 == 0
  
  if even == False:
    return 'invalid'
​
  subsets = []
  
  for n in range(1, len(s), 2):
    subset = [s[n-1], s[n]]
    subsets.append(subset)
  
  final_str = ''
  
  for subset in subsets:
    count = int(subset[0])
    num = str(subset[1])
    
    for n in range(count):
      final_str += num
  
  return int(final_str)

