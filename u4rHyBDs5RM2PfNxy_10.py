
def count_ones(lst):
  string = ''
  for i in lst:
    if str(i) in '10':
      string += str(i)
  print(string)
  ones = string.split('0')
  print(ones)
  output = [segment for segment in ones if len(segment)>1]
  return len(output)

