
def cutting_grass(lst, *cuts):
  results = []
  curLen = lst
  for cut in cuts:
    cutted = [x-cut for x in curLen]
    if any(x <= 0 for x in cutted):
      results.append("Done")
      curLen = cutted
    else:
      results.append(cutted)
      curLen = cutted
  return results

