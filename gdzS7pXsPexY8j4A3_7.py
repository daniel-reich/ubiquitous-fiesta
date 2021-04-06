
def count_digits(lst, t):
  even_or_odd_count = []
  if t == "even":
    count = 0
    for num in lst:
      temp_lst = [int(num) for num in str(num)]
      for digit in temp_lst:
        if digit % 2 == 0:
          count += 1
      even_or_odd_count.append(count)
      count = 0
  if t == "odd":
    count = 0
    for num in lst:
      temp_lst = [int(num) for num in str(num)]
      for digit in temp_lst:
        if digit % 2 != 0:
          count += 1
      even_or_odd_count.append(count)
      count = 0
  return even_or_odd_count

