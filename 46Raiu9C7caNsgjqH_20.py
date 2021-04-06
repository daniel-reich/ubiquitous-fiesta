
def compare_data(*args):
  return len(set(map(type,args))) < 2

