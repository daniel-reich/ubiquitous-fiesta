
def rearranged_difference(num):
  ind = 0
  loopcount = 0
  ls = [int(i) for i in str(num)]
  while loopcount < len(ls):
    for i in ls:
      if (ind + 1) < len(ls):
        if i < ls[ind + 1]:
          x = ls.index(i)
          ls[x], ls[ind+1] = ls[ind+1], ls[x]
        ind += 1
    ind = 0
    loopcount += 1
​
  large_val = "".join(str(i) for i in ls)
  small_val = "".join(str(i) for i in list(reversed(ls)))
  return(int(large_val) - int(small_val))

