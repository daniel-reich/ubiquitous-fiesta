
def daily_streak(lst):
  current_streak,max_streak = 0,0
  for x in lst:
    if x: current_streak += 1
    else: current_streak = 0
    
    if current_streak > max_streak: max_streak = current_streak
  
  return max_streak

