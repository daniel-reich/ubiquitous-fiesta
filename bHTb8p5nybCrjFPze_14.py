
def inclusive_list(start_num, end_num):
  if start_num>end_num:
    return [start_num]
  else:
    return generate_list(start_num, end_num)
​
def generate_list(ini, end):
  response = []
  for number in range(ini,end+1):
    response.append(number)
  return response

