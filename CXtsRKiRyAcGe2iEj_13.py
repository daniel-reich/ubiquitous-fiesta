
def time_to_finish(full, part):
  return (sum(1 for i in full if i != " ") - sum(1 for i in part if i != " "))/2

