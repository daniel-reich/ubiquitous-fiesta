
def over_time(lst):
  reg=(lst[1]-lst[0])*lst[2]
  return '${:,.2f}'.format(reg+(min([lst[1]-17,lst[1]-lst[0]])*lst[3]*lst[2])-(min([lst[1]-17,lst[1]-lst[0]])*lst[2])) if lst[1]>17 else '${:,.2f}'.format(reg+.001)

