
def number_of_repeats(s):
  repeat = s[0]
  for i in range(len(s)-1):
    if repeat == s[i+1:len(repeat)+i+1]:
      break
    else:
      repeat += s[i+1]
  return len(s) / len(repeat)

