
def longest_substring(digits):
  biggest_sub, current_sub = "", "" 
  for i in range(len(digits)-1):
    if (int(digits[i])%2 == 0 and int(digits[i+1])%2 == 1) or (int(digits[i])%2 == 1 and int(digits[i+1])%2 == 0):
      current_sub += digits[i]
    else:
      if len(current_sub) == 0:
        continue
      if (int(current_sub[len(current_sub)-1])%2 == 0 and int(digits[i])%2 == 1) or (int(current_sub[len(current_sub)-1])%2 == 1 and int(digits[i])%2 == 0):
        current_sub += digits[i]
        if len(current_sub) > len(biggest_sub):
          biggest_sub = current_sub
          current_sub = ""
        else:
          current_sub = ""
      elif len(current_sub) > len(biggest_sub):
        biggest_sub = current_sub
        current_sub = ""
  if len(current_sub) != 0 and ((int(current_sub[len(current_sub)-1])%2 == 0 and int(digits[len(digits)-1])%2 == 1) or (int(current_sub[len(current_sub)-1])%2 == 1 and int(digits[len(digits)-1])%2 == 0)):
    current_sub += digits[len(digits)-1]
  if len(current_sub) > len(biggest_sub):
    return current_sub
  return biggest_sub

