
'''
Create a function that determines whether a number is Oddish or Evenish.
A number is Oddish if the sum of all of its digits is odd, and a number 
is Evenish if the sum of all of its digits is even. 
If a number is Oddish, return "Oddish". Otherwise, return "Evenish".
'''
def oddish_or_evenish(num):
  tot = 0 
  for nums in str(num):
    tot += int(nums)
  return "Evenish" if tot%2 == 0 else "Oddish"

