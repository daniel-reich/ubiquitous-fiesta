
def alternate_sort(lst):
  numbers = sorted([i for i in lst if type(i)==int])
  letters = sorted([i for i in lst if type(i)==str])
  output = []
  for i in range(len(numbers)):
    output.append(numbers[i])
    output.append(letters[i])
  return output

