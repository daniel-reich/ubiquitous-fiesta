
def bar_chart(results):
  sorted_results = sorted(results.items(), key=lambda x: (x[1]*-1, x[0]))
  bar_chart_list = [i[0] + '|' + '#'*(i[1]//50) + (' ' if i[1]>0 else '') + str(i[1]) + '\n' for i in sorted_results]
  return ''.join(bar_chart_list).strip()

