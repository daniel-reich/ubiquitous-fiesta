
def get_filename(path):
  a = ""
  if "/" in path:
    a = path.split("/")
    return a[-1]
  else:
    return path

