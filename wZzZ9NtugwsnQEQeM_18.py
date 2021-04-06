
def golf_score(course, result):
  return sum([course[x]-list(map(lambda x: 2 if x == "eagle" else 1 if x == "birdie" else -1 if x == "bogey" else -2 if x == "double-bogey" else 0, result))[x] for x in range(len(course))])

