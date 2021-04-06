
def ascii_sort(lst):
  sum_of_word_one = 0
  sum_of_word_two = 0
  for char in lst[0]:
    sum_of_word_one += ord(char)
  for char in lst[1]:
    sum_of_word_two += ord(char)
  return lst[0] if sum_of_word_one < sum_of_word_two else lst[1]

