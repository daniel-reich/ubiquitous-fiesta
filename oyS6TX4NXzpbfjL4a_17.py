
def best_start(lst, word):
  word_to_score = {'A':1,'B':3,'C':3,'D':2,'E':1,'F':4,'G':2,'H':4,'I':1,'J':8,'K':5,'L':2,'M':3,'N':1,'O':1,'P':3,
                'Q':10,'R':1,'S':1,'T':1,'U':1,'V':4,'W':4,'X':8,'Y':4,'Z':10,'-':1,'DL':2,'TL':3,'DW':1}
  time = len(lst)-len(word)+1
  index_score = {}
  for i in range(time):
    total_score = 0
    double = False
    for j in range(len(word)):
      char = word[j].upper()
      pos = lst[j+i]
      if pos == 'DW':
        double = True
      total_score += word_to_score[char] * word_to_score[pos]
    if double:
      total_score = total_score*2
    index_score[i] = total_score
  max_score=0
  max_index = None
  for index,score in index_score.items():
    if score>max_score:
      max_score = score
      max_index = index 
  return max_index

