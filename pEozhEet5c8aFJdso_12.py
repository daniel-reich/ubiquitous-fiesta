
def all_about_strings(txt):
  lst = []
  # Length
  lst.append(len(txt))
  # First character
  lst.append(txt[0])
  # Last character
  lst.append(txt[-1])
  # Middle character or middle two characters
  if len(txt) % 2 == 0:
    lst.append(txt[len(txt) // 2 - 1] + txt[len(txt) // 2])
  if len(txt) % 2 != 0:
    lst.append(txt[len(txt) // 2])
  # Index of the second occurence of the second character
  # "@ index #" or "not found"
  txt_check = txt[2:]
  index_count = 2
  for char in txt_check:
    if txt[1] not in txt_check:
      lst.append("not found")
      break
    elif char == txt[1]:
      lst.append("@ index {}".format(index_count))
    index_count += 1
  return lst

