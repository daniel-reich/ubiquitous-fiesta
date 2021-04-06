
def is_prime( num ):
    return bool( num % 2 ) and all( num % x for x in range(3, int(num**0.5)+1, 2))
def value( word ):
    return sum( ord(ch)-(ord('a')-1 if ch.isalpha() else ord('0')) for ch in word.lower() if ch.isalnum())
​
def sentence_primeness(sent):
    words_value = list( value(w) for w in sent.split())
    sent_value = sum(words_value)
    if is_prime( sent_value): return 'Prime Sentence'
    almost_prime = list(is_prime(sent_value - x) for x in words_value)
    if True in almost_prime:
      w = sent.split()[almost_prime.index(True)]
      w = ''.join(x for x in w if x == ' ' or x.isalnum())
      return 'Almost Prime Sentence (%s)' % (w)
    return 'Composite Sentence'

