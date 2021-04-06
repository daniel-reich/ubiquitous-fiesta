
def time_to_finish(full, part):
  fin = full[len(part):].split()
  return sum([len(i) for i in fin])*0.5

