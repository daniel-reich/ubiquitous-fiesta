
def lcm_three(num):
  i = max(num)
  while True: 
    if(i % num[0] == 0 and i % num[1] == 0 and i % num[2] == 0):
      print(i)
      #break
      return i
    i = i + 1

