
def get_gcd(a,b): 
  [sml,lar] = sorted([a,b])
  startoff = sml
  while startoff > 0: 
    if lar % startoff == 0 and sml % startoff == 0:
      print(str(lar) + ' divided by ' + str(startoff) + ' = ' + str(lar/startoff))
      
      print(startoff)
      return startoff
    startoff -= 1
  return 1
    
​
def lcm_of_list(numbers):
  lcm = numbers[0]
  for i in range(1,len(numbers)):
    print(lcm)
    print(numbers[i])
    lcm = lcm * numbers[i]//get_gcd(lcm,numbers[i])
    print(lcm)
    print('-----')
  return lcm

