
def win_round(you, opp):
  you.sort(reverse=True)
  opp.sort(reverse=True)
  you_num = str(you[0]) + str(you[1])
  opp_num = str(opp[0]) + str(opp[1])
  return int(you_num) > int(opp_num)

