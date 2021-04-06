
ONES = "zero one two three four five six seven eight nine ten eleven twelve thirteen fourteen fifteen sixteen seventeen eighteen nineteen".split()
TENS = "twenty thirty forty fifty sixty seventy eighty ninety".split()
​
def eng2nums(s):
  n = 0
  for w in s.split():
    if w in ONES: n += ONES.index(w)
    if w in TENS: n += (TENS.index(w) + 2) * 10
    if w == "hundred": n *= 100
  return n

