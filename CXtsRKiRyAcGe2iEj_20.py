
def time_to_finish(full, part):
  return (len(full)-len(part)-full[len(part):].count(" "))*0.5

