
import re
​
def sentence_primeness(sentence):
  words_and_numbers  = re.split(r"[^a-zA-Z0-9]+" , sentence);
  word_values  = [get_word_value(word_or_num) for word_or_num in words_and_numbers ];
  
  sentence_value  = sum(word_values);
  if (is_prime(sentence_value)):
    return "Prime Sentence";
  
  almost_prime_words  = [word for word in words_and_numbers if is_prime(sentence_value - get_word_value(word))]
  return "Almost Prime Sentence ({})".format(almost_prime_words[0]) if almost_prime_words else  "Composite Sentence";
​
def get_word_value(word):
  return sum([ord(e.lower()) - ord("a")+1 if e.isalpha() else int(e) for e in word])
​
def is_prime(num):
  return all([num%k != 0  for k in range(2, num//2 + 1)]);
  
def get_digits(num):
  return [int(d) for d in str(num)];

