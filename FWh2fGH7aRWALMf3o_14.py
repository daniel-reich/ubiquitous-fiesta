
def cleave(string, lst):
  if len(string) == 0:
    return ""
  results = recursiveCleave(string, lst)
  if( len(results) == 0 ):
    return "Cleaving stalled: Word not found"
  else:
    return results[0]
def recursiveCleave(string, lst):
  if len(string) == 0:
    return [""]
  potentialBreaks = []
  for endIndex in range(len(string)+1):
    subStr = string[:endIndex]
    if subStr in lst:
      potentialBreaks += [ endIndex ]
  potentialResults = []
  for potentialBreak in potentialBreaks:
    otherHalf = recursiveCleave(string[potentialBreak:], lst)
    for results in otherHalf:
        if( len(results) != 0 ):
          potentialResults += [ string[:potentialBreak] + " " + results ]
        else:
          potentialResults += [ string[:potentialBreak]]
  return potentialResults

