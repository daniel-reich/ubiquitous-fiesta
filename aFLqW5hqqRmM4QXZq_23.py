
def string(n):
  if n == 0:
    return "0"
  else:
    return " " + str(n)
def bar_chart(results):
  results = sorted([(v,k) for k,v in results.items()], reverse = True, key = lambda tup: tup[0] - int(tup[1][-1]))
  return "\n".join([result[1] + "|" + "#"*(result[0]//50) + string(result[0]) for result in results])

