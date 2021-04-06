
def find_zip(string):
  string = string.replace("zip", "---", 1)
  try:
    x = string.index("zip")
    return (x)
  except ValueError:
    return (-1)

