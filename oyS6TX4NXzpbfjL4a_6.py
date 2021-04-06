
def best_start(lst, word):
 score_dict={'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':2,'M':3,'N':1,'O':1,'P':3,'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10}
 caps=word.upper()
 # print(caps)
 high=0
 # go through list until index = len of list- len of word VERIFY RANGE!
 for i in range(0,len(lst)-len(word)):
  # print('i', i)
  # create sum for word if starting at current index 
  score=0
  double=False
  for k in range(0,len(word)):
   # print('k',k)
   if lst[i+k] == "DL":
    score+=score_dict[caps[k]]*2
    # print('score ',score)
   elif lst[i+k] == "TL":
    score+=score_dict[caps[k]]*3
    # print('score ',score)
   elif lst[i+k] == "DW":
    score+=score_dict[caps[k]]
    # print('score ',score)
    double=True
    # print('double')
   else:
    score+=score_dict[caps[k]]
    # print('score ',score)
  if double:
   score*=2
  # print('score', score)
  # if greater than current max 
  if score > high:
   high = score
   # print('high ', high)
   # index == current iterator (e.g. i)
   index=i
   # print('index ',index)
 return index

