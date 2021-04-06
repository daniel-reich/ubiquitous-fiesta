
def get_filename(path):
  if "/" in path:
    return path.split("/")[-1]
  return path

