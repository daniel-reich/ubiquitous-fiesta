
def word_to_decimal(word):
  nums = word.lower()[::-1]
  base = 10 + ord(max(nums))-96
  return sum((ord(c)-87) * base**i for i, c in enumerate(nums))

