
def yahtzee_score_calc(lst):
  c = 0
  
  for idx, turn in enumerate(lst):
    ranks = set(turn)
    freq = sorted(turn.count(r) for r in ranks)
    s = ''.join(str(d) for d in sorted(ranks))
    
    dic = {
      0: sum(i for i in turn if i == idx+1),
      6: sum(turn) * (freq[-1] >= 3),
      7: sum(turn) * (freq[-1] >= 4),
      8: 25 * (freq == [2, 3]),
      9: 30 * any(i in s for i in ('1234', '2345', '3456')),
      10: 40 * any(i in s for i in ('12345', '23456')),
      11: 50 * (len(ranks) == 1),
      12: sum(turn)
    }
    
    if idx < 6: c += dic[0]
    if idx == 6: c += 35 * (c >= 63)
    if idx >= 6: c += dic[idx]
    
  return c

