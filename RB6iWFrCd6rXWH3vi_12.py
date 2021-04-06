
def longest_substring(digits):
  ix = 0
  while True:
    if (int(digits[ix]) + int(digits[ix + 1])) % 2 == 1:
      ix += 1
    else:
      break
  last_s = 0
  last_e = ix
  max_s = 0
  max_e = last_e
  ix += 1
  while True:
    if ix == len(digits) - 2:
      if (int(digits[ix]) + int(digits[ix + 1])) % 2 == 0:
        last_s = last_e + 1
        last_e = ix
        if last_e - last_s > max_e - max_s:
          max_e = last_e
          max_s = last_s
      else:
        last_s = last_e + 1
        last_e = ix + 1
        if last_e - last_s > max_e - max_s:
          max_e = last_e
          max_s = last_s
      break
    else:
      if (int(digits[ix]) + int(digits[ix + 1])) % 2 == 0:
        last_s = last_e + 1
        last_e = ix
        if last_e - last_s > max_e - max_s:
          max_e = last_e
          max_s = last_s
      ix += 1
  return digits[max_s:max_e + 1]

