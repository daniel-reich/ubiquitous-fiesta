
def sort_decending(num):
  num = str(num)
  numlist = list(num)
  numlist.sort()
  outtext = ''
  for i in numlist[::-1]:
    outtext += i
  return int(outtext)

