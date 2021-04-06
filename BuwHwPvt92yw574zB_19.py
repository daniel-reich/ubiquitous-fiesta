
def list_of_multiples(num, length):
  count = 1
  nums = []
  while count <= length:
    nums.append(num*count)
    count = count + 1
  return nums

