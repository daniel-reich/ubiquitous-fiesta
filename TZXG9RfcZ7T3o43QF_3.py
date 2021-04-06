
def same_length(txt):
  ones = [i for i in txt.split('0') if i != '']
  zeroes = [i for i in txt.split('1') if i != '']
  if len(ones) != len(zeroes):
    return False
  for i in range(len(ones)):
    if len(ones[i]) != len(zeroes[i]): 
      return False
  return True

