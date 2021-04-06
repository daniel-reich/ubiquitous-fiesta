
def num_to_google(lst):
  lst = [str(i) for i in lst]
  chars = {"1":"g","2":"o","3":"l","4":"e","6":"."}
  output = ""
  for i in lst:
    next_item = ""
    for j, k in enumerate(i):
      if k in chars.keys():
        next_item += chars[k]
      elif k == "5":
        next_item = next_item[:-1] + next_item[-1].swapcase()
      elif k == "7":
        next_item = next_item[0].swapcase() + next_item[1:]
      elif k == "8":
        next_item = next_item[::-1]
      elif k == "9":
        next_item = ""
        break
      else:
        next_item *= int(i[j+1:])
        break
    output += next_item
  return output

