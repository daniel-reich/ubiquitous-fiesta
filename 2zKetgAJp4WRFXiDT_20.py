
def number_length(num):
  cnt = 1
  while num >= 10:
    num /= 10
    cnt += 1
  return cnt

