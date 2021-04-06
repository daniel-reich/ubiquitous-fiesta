
def yahtzee_score_calc(lst):
  first_six = sum(x for i in range(6) for x in lst[i] if x==i+1)
  bonus = 35*(first_six>=63)
  three_kind = sum(lst[6])*any(lst[6].count(l)>=3 for l in lst[6])
  four_kind = sum(lst[7])*any(lst[7].count(l)>=4 for l in lst[7])
  full = 25*(sorted([lst[8].count(l) for l in lst[8]])==[2,2,3,3,3])
  lower = 30*any(all(i+j in lst[9] for j in range(4)) for i in [1,2,3])
  higher = 40*any(all(i+j in lst[10] for j in range(5)) for i in [1,2])
  yahtzee = 50*(len(set(lst[11]))==1)
  chance = sum(lst[12])
  return first_six+bonus+three_kind+four_kind+full+lower+higher+yahtzee+chance

