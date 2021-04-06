
def closest_palindrome(num):
  if str(num) == str(num)[::-1]:
    return num
  num_upper = num
  while str(num_upper) != str(num_upper)[::-1]:
    num_upper += 1
  num_lower = num
  while str(num_lower) != str(num_lower)[::-1]:
    num_lower -= 1
  dist_upper = abs(num_upper - num)
  dist_lower = abs(num - num_lower)
  if dist_upper == dist_lower:
    return num_lower
  if dist_upper < dist_lower:
    return num_upper
  if dist_lower < dist_upper:
    return num_lower

