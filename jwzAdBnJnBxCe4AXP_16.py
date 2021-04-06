
def rearranged_difference(num):
  sorted_num = int("".join(sorted(str(num))))
  reversed_num = int("".join(reversed(sorted(str(num)))))
  return reversed_num - sorted_num

