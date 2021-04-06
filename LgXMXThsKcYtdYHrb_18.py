
def split_and_delimit(txt, num, delimiter):
  result = ""
  counter = 0
  for c in txt:
    if counter == num:
      result += delimiter
      counter = 0
    result += c
    counter += 1
  
  return result

