
def golf_score(course, result):
  newlist = []
  for i in range(len(course)):
    if result[i] == 'eagle':
      newlist.append(course[i] - 2)
    elif result[i] == 'birdie':
      newlist.append(course[i] - 1)
    elif result[i] == 'bogey':
      newlist.append(course[i] + 1)
    elif result[i] == 'double-bogey':
      newlist.append(course[i] + 2)
    elif result[i] == 'par':
      newlist.append(course[i])
  return sum(newlist)

