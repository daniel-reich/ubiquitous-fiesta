
def number_of_repeats(s):
  for i in range(1,len(s)):
    a=[s[j:j+i] for j in range(0,len(s),i)]
    if all(ele==a[0] for ele in a): return len(a)
  return 1

