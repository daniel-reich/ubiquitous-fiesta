
def win_round(you, opp):
  my_tens = max(you)
  you_copy = you.copy()
  you_copy.remove(my_tens)
  my_ones = max(you_copy)
  my_num = my_tens*10 + my_ones
  
  opp_tens = max(opp)
  opp_copy = opp.copy()
  opp_copy.remove(opp_tens)
  opp_ones = max(opp_copy)
  opp_num = opp_tens*10 + opp_ones
  
  if my_num > opp_num:
    return True
  else:
    return False

