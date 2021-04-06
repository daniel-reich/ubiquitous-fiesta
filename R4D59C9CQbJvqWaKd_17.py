
def batting_avg(lst):
  return str(round(sum(i[0] for i in lst) / sum(i[1] for i in lst), 3)).ljust(5, "0")[1:]

