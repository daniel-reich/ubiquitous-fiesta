
def in_box(lst):
  for line in lst[1:-1]:
    if '*' not in line:
      continue
    line = line.replace(' ', '')
    if '#*#' in line:
      return True
  return False

