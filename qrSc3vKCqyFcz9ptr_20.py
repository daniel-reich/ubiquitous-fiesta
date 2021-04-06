
def sum_round(num):
  nums = []
  num = str(num)[::-1]
  for i, digit in enumerate(num):
    if digit == "0":
      continue
    power = pow(10, i)
    nums.append(str(int(digit)*power))
  return " ".join(nums)

