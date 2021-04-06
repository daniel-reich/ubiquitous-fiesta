
def is_goal_scored(goal):
  return (["  #0    #  "] in goal) or (["  # 0   #  "] in goal) or (["  #  0  #  "] in goal) or (["  #   0 #  "] in goal) or (["  #    0#  "] in goal)

