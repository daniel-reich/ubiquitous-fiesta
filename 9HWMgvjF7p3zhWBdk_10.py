
def keys_and_values(d):
  result = []
  result.append([])
  result.append([])
  for key in sorted(d):
    result[0].append(key)
    result[1].append(d[key])
  return result

