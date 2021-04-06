
def scale_tip(lst):
  l_sum=sum(lst[:((len(lst)+1)//2)-1])
  r_sum=sum(lst[((len(lst)+1)//2):]) 
  return "left" if l_sum>r_sum else "right" if r_sum>l_sum else "balanced"

