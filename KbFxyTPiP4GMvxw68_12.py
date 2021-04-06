
def longest_zero(s):
  zeroes = ""
  while True:
    if zeroes in s:
      zeroes += "0"
      continue
    else:
      return zeroes[1:]

