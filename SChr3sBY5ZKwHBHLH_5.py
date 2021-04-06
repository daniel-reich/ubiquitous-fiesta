
def sort_it(lst):
  ints = [i for i in lst if type(i) == int]
  lists = [i[0] for i in lst if type(i) == list]
  output = ints + lists
  output.sort()
  for i in range(len(output)):
    if output[i] in lists:
      output[i] = [output[i]]
  return output

