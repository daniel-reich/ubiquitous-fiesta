
def EPLResult(table, team):
  x = table[:]
  newlist = []
  goal_diff_dict = {}
  points_amount = {}
  positions = {1: '1st', 2: '2nd', 3: '3rd', 4: '4th', 5: '5th', 6: '6th', 7: '7th', 8: '8th', 9: '9th', 10: '10th', 11: '11th', 12: '12th', 13: '13th', 14: '14th', 15: '15th', 16: '16th', 17: '17th', 18: '18th', 19: '19th', 20: '20th', 21: '21st', 22: '22nd'}
  for eachteam in x:
    total_points = 0
    goal_diff_dict[eachteam[0]] = eachteam[-1]
    total_points += eachteam[2]*3 + eachteam[3]
    newlist.append([eachteam[0],total_points])
  z = sorted(newlist, key = get_points)[::-1]
  for x,y in z:
    points_amount[x] = y
  newlist3 = []
  team_points = 0
  behind_them = 0
  curr_team = []
  for eachteam in z:
    if eachteam[0] == team:
      newlist3.append(eachteam)
      team_points = eachteam[1]
      curr_team = eachteam
      break
  for eachteam in z:
    if eachteam[0] != team and eachteam[1] == team_points:
      newlist3.append(eachteam)
  if len(newlist3) == 1:
    return '{} came {} with {} points and a goal difference of {}!'.format(newlist3[0][0],positions[z.index(newlist3[0])+1],newlist3[0][1],goal_diff_dict[newlist3[0][0]])
  else:
    curr_team_diff = goal_diff_dict[team]
    curr_team_points = points_amount[team]
    for eachteam in newlist3:
      if goal_diff_dict[eachteam[0]] > curr_team_diff:
        behind_them += 1
      elif goal_diff_dict[eachteam[0]] < curr_team_diff and z.index(eachteam) < z.index(curr_team):
        behind_them -= 1
    return '{} came {} with {} points and a goal difference of {}!'.format(newlist3[0][0],positions[z.index(newlist3[0])+1+behind_them],newlist3[0][1],goal_diff_dict[newlist3[0][0]])
    
  
  
def get_points(eachteam):
  return eachteam[1]

