
def yahtzee_score_calc(lst):
  score = 0
  score+=lst[0].count(1)
  score+=lst[1].count(2)*2
  score+=lst[2].count(3)*3
  score+=lst[3].count(4)*4
  score+=lst[4].count(5)*5
  score+=lst[5].count(6)*6
  if score>=63:
    score+=35
  if any([lst[6].count(i)>=3 for i in lst[6]]):
    score+=sum(lst[6])
  if any([lst[7].count(i)>=4 for i in lst[7]]):
    score+=sum(lst[7])
  if len(set(lst[8]))==2 and any([lst[8].count(i)==3 for i in lst[8]]):
    score+=25
  if len(set(lst[9]))>=4:
    if all([i in lst[9] for i in [1,2,3,4]]) or all([i in lst[9] for i in [2,3,4,5]]) or all([i in lst[9] for i in [3,4,5,6]]):
      score+=30
  if len(set(lst[10]))>=5:
    if all([i in lst[10] for i in [1,2,3,4,5]]) or all([i in lst[10] for i in [2,3,4,5,6]]):
      score+=40
  if len(set(lst[11]))==1:
    score+=50
  score+=sum(lst[12])
  return score

