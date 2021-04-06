
def delete_occurrences(lst, num):
  output = [] 
  for i in lst:
    if output.count(i) < num:
      output.append(i)
  return output

