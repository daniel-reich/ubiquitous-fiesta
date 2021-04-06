
import re
​
def most_common_words(text , n) :
  words  = re.findall( r"\w+" ,text.lower());
  d = dict([ (word , words.count(word)) for word in words]);
  return {key:d[key] for key in sorted(d , key = lambda k : (d[k] , -words.index(k)) , reverse = True)[0:n]};

