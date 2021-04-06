
def rearranged_difference(num):
  lst = [i for i in str(num)]
  lst.sort()
  small = ''.join(lst)
  lst.sort(reverse=True)
  big = ''.join(lst)
  return int(big) - int(small)

