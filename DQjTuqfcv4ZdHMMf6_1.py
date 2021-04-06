
def kaprekar(num):
  if num == 6174:
    return 0
​
  mn = "".join(sorted(str(num))).zfill(4)
  mx = mn[::-1]
  return 1 + kaprekar(int(mx) - int(mn))

