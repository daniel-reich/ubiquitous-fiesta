
def box_seq(step):
  result = 0
  for i in range(1, step + 1):
    if i % 2 != 0:
      result += 3
    else:
      result -= 1
      
  return result

