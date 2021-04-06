
def eng2nums(s):
  numbers = {
    'one': 1, 'two': 2, 'three': 3, 'four': 4, 'five': 5, 'six': 6,
    'seven': 7, 'eight': 8, 'nine': 9, 'ten': 10, 'eleven': 11,
    'twelve': 12, 'thirteen': 13, 'fourteen': 14, 'fifteen': 15,
    'sixteen': 16, 'seventeen': 17, 'eighteen': 18, 'nineteen': 19,
    'forty': 40, 'fifty': 50, 'twenty': 20, 'thirty': 30,
    'sixty': 60, 'seventy': 70, 'eighty': 80, 'ninety': 90,
    'hundred': 100, 'zero': 0
  }
  words = [numbers.get(word, word) for word in s.split()]
  result = 0
  for index, word in enumerate(words):
    if word == 100:
      result *= 100
    else:
      result += word
  return result

