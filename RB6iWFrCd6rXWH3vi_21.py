
def longest_substring(digits):
  flag = int(digits[0])%2 # 1 - odd | 0 - even
  temp = [digits[0]]
  final = []
  for dig in digits:
    if int(dig) % 2 != flag:
      temp += [dig]
      flag = int(dig) % 2
    else:
      if len(final) < len(temp):
        final = temp
        temp = [dig]
      else:
        temp = [dig]
    if len(final) < len(temp):
        final = temp
  return "".join(final)

