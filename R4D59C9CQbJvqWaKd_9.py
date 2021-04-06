
def batting_avg(lst):
  hits = sum([i[0] for i in lst])
  at_bats = sum([i[1] for i in lst])
  av = round(hits/at_bats, 3)
  return str(av).lstrip("0") + "0" if len(str(av)) == 4 else str(av).lstrip("0")

