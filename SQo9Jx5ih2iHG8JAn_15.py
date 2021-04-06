
def expanded_form(num):
  num_arr = [int(e) for e in str(num)]
  
  num_str = ""
  for i, num in enumerate(num_arr):
    if num != 0:
      if i != 0:
        num_str += " + "
      num_str += str(num * (10**(len(num_arr)-1-i)))
      
  return num_str

