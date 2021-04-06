
def join(lst):
  shared = []
  string = ''
  for pair in zip(lst, lst[1:]):
    for ind, l in enumerate(pair[0]):
      if pair[0][ind:] in pair[1]:
        shared.append(len(pair[0][ind:]))
        break 
      string += l
  return [string+lst[-1], 0 if not shared else min(shared)]

