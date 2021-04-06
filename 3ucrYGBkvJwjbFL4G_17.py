
def reversible_inclusive_list(start, end,i=1):
    if start == end: return [start]
    if start > end: return ([end] + reversible_inclusive_list(end+1,start))[::-i]
    return [start] + reversible_inclusive_list(start+1, end)

