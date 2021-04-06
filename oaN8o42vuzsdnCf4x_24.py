
from functools import partial,reduce
from operator import getitem
​
scores = {'a':1,'b':3,'c':3,'d':2,'e':1,'f':4,'g':2,'h':4,'i':1,'j':8,'k':5,'l':2,'m':3,'n':1,'o':1,'p':3,'q':10,'r':1,'s':1,'t':1,'u':1,'v':4,'w':4,'x':8,'y':4,'z':10}
​
def get_score(word):
  return sum(map(partial(getitem,scores),word))
​
def best_words(lst):
  value=max(map(get_score,lst))
  return [word for word in lst if get_score(word)==value]

