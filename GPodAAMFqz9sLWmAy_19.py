
def one_odd_one_even(n):
  nums = list(map(int, str(n)))
  counter = [0,0]
  for n in nums:
    if n % 2 == 0:
      counter[0] = 1
    elif n % 2 != 0:
      counter[1]= 1
  return counter == [1,1]

