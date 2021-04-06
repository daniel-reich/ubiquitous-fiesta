
def next_number(num):
  n = [int(i) for i in str(num)]
  for i in range (2,len(n)+1):
    if n[-i] < n[1-i]:
      tail = n[-i:].copy()
      tail.sort()
      digit = 0
      for j in tail:
        if j > n[-i] and (digit==0 or j < digit):
          digit = j
      n[-i] = digit
      tail.remove(digit)
      n[1-i:] = tail
      break
  num = ""
  for i in n:
    num += str(i)
  return int(num)

