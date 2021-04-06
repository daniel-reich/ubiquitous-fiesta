
def time_to_finish(full, part):
  return len([i for i in full[len(part):] if i!=' '])/2

