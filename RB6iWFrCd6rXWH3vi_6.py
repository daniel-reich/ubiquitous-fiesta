
def longest_substring(digits):
  n_digits = ''.join([str(int(x)%2) for x in digits])
  index_len = {}
  for i in range(len(n_digits)-1):
    l = 0
    for ii in range(len(n_digits[i:])-1):
      if n_digits[i+ii] != n_digits[i+ii+1]:
        l += 1
      else:
        break
    index_len[i] = l
  w_d = max(index_len, key=index_len.get)
  return digits[w_d:1 + w_d + index_len[w_d]]

