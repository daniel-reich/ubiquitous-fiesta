
def lcm_three(num):
  i = 1
​
  while not(((max(num) * i % num[0] == 0) & (max(num) * i % num[1] == 0) & (max(num) * i % num[2] == 0))):
    i += 1
​
  return max(num) * i

