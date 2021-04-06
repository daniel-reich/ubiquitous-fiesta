
def closest_palindrome(num):
  if str(num) == str(num)[::-1]:
    return num
  temp1,temp2 = num,num
  while str(temp1) != str(temp1)[::-1]:
    temp1 += 1
  while str(temp2) != str(temp2)[::-1]:
    temp2 -= 1
    
  if abs(num-temp1) != abs(num-temp2):
    return min(temp1,temp2, key = lambda x: abs(num-x))
  else:
    return min(temp1,temp2)

