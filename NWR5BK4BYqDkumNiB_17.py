
def digital_division(n):
  count = 0
  final = 0
  total_sum = 0
  total_product = 1
  perfect = "Perfect"
  indivisible = "Indivisible"
  num1 = 1
  num2 = 2
  ls = [ch for ch in str(n)]
  if '0' in ls:
    ls.remove('0')
  if n == 100:
    ls.remove('0')
  for elem in ls:
    if n % int(elem) == 0:
      count = count + 1
  if count == int(len(ls)):
    final = final + 1
  # part 2
  for elem in ls:
    total_sum = total_sum + int(elem)
  if n % total_sum == 0:
    final = final + 1
​
  # part 3
  ls = [ch for ch in str(n)]
  if '0' in ls:
    final = final
  else:
    for elem in ls:
      total_product = total_product*int(elem)
  
    if n % total_product == 0:
      final = final + 1
  # last part
  if final == 3:
    return perfect
  if final == 2:
    return num2
  if final == 1:
    return num1
  if final == 0:
    return indivisible

