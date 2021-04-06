
def batting_avg(lst):
 first = sum([x[0] for x in lst])
 last = sum([x[1] for x in lst])
 return str(round(first/last,3))[1:].ljust(4,"0")

