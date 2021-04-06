
def max_occur(text):
  max_number = 0
  for eachletter in text:
    if text.count(eachletter) > max_number:
      max_number = text.count(eachletter)
  if max_number == 1:
    return 'No Repetition'
  return list([x for x in set(list([x for x in text if text.count(x) == max_number]))])

