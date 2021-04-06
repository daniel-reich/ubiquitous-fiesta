
import re
​
def sentence_primeness(sentence):
  total_sum = 0
  words = re.sub(r'[^a-zA-Z0-9 ]', '', sentence).split(' ')
​
  def get_sum(word):
    ret = 0
    for letter in word:
      if letter.isdigit():
        ret += int(letter)
      else:
        ret += ord(letter.lower()) - ord('a') + 1
    return ret
​
  def is_prime(number):
    for i in range(2, number//2):
      if number % i == 0:
        return False
    return True
​
  for word in words:
    total_sum += get_sum(word)
​
  if is_prime(total_sum):
    return "Prime Sentence"
  else:
    for word in words:
      if is_prime(total_sum - get_sum(word)):
        return "Almost Prime Sentence ({})".format(word)
  return "Composite Sentence"

