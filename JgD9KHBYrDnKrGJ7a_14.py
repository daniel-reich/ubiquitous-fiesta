
def swap_dict(dic):
  output = {}
  for i in dic:
    if dic[i] not in output:
      output[dic[i]] = [i]
    else:
      output[dic[i]].append(i)
  return output

