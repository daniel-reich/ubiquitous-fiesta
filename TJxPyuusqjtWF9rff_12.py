
def get_only_evens(nums):
    x = 0
    y = []
    for num in nums:
      if num % 2 == 0 and x % 2 == 0:
        y.append(num)
      x += 1
    return y

