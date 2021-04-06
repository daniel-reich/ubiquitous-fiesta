
def divisible_by_left(n):
  
  seperated = []
  for i in str(n):
    seperated.append(i)
​
  first = 0
  second = 0
  final = []
​
  for i in seperated:
    second = int(i)
    if first == 0 :
      final.append(False)
    elif (second % first) == 0:
      final.append(True)
    else:
      final.append(False)
    first = second
​
  print(final)
  return final
​
divisible_by_left(73312)

