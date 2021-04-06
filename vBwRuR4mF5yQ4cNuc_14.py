
def count_missing_nums(lstNum):
  filterList = [int(i) for i in lstNum if i.isdigit()]
  countMissing = [i for i in range(min(filterList), max(filterList) + 1) if i not in filterList]
  return len(countMissing)

