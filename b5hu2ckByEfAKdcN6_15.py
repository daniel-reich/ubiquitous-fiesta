
def reverse_and_not(i):
  number = str(i)
  num_list = []
  for digit in number:
    num_list.append(digit)
  num_list.reverse()
  num_string = ''
  for digit in num_list:
    num_string += digit
  return int(num_string + number)

