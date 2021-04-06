
def longest_substring(digits):
  current = longest = digits[0]
  for digit in digits[1:]:
    if int(digit)%2 != int(current[-1])%2:
      current += digit
    else:
      longest = longest if len(longest) >= len(current) else current
      current = digit
  longest = longest if len(longest) >= len(current) else current
  return longest

