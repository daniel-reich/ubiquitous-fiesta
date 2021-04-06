
def rearranged_difference(num):
  string = str(num)
  maximum = int("".join(sorted(string, reverse = True)))
  minimum = int("".join(sorted(string)))
  return maximum - minimum

