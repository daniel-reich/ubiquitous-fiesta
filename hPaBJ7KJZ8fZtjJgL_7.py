
def how_many_times(num):
  st = "Edabit"
  lis = st.split('a')
  if num <= 0:
    return ''.join(lis)
  else:
    return lis[0]+num * "a"+lis[1]

