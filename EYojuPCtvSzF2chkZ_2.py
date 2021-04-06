
def get_filename(path):
  return path if '/' not in path else path.split('/')[-1]

