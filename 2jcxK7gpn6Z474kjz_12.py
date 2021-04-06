
def security(txt):
  filtered = [char for char in txt if char in 'TG$']
  for index, char in enumerate(filtered):
    if char != '$':
      continue
    if index > 0 and filtered[index - 1] == 'T':
      return 'ALARM!'
    if index < len(filtered) - 1 and filtered[index + 1] == 'T':
      return 'ALARM!'
  return 'Safe'

