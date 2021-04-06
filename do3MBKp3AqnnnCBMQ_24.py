
import random
def numbers():
  nums = ['1', '2', '3', '4', '5']
  random.shuffle(nums)
  return int(''.join(nums))

