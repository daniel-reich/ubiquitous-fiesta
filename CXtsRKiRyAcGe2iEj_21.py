
def time_to_finish(full, part):
  comp = len([i for i in full if i != " "])
  incomp = len([i for i in part if i != " "])
  return (comp-incomp) * 0.5

