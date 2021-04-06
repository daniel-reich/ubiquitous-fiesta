
def print_all_groups():
  lst = []
  for n in range(1, 7):
    for letter in ["a", "b", "c", "d", "e"]:
      lst.append(str(n)+letter)
  return ", ".join(lst)

