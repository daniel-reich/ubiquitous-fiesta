
def track_robot(instructions):
  result = [0,0]
  tmp = [0,0,0,0]
  for i in instructions:
    d = i[0]
    v = int(i.split(" ")[1])
    print ("d :",d)
    print ("v : ",v)
    if d == 'r':
      tmp[0] += v
    if d == 'l':
      tmp[1] += v
    if d == 'u':
      tmp[2] += v
    if d == 'd':
      tmp[3] += v
​
  result[0] = tmp[0] - tmp[1]
  result[1] = tmp[2] - tmp[3]
  return result

