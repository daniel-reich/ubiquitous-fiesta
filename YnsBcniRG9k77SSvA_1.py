
def print_all_groups():
  result = []
  for i in '123456':
    for x in 'abcde':
      result.append(i+x)
  return ', '.join(result)

