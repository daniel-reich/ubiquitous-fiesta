
def final_countdown(lst):
  count = 0
  countdown = []
  countdown_lst = []
  if lst:
    for i in range(len(lst)):
      if i == 0 or (lst[i])+1 == lst[i-1]:
        countdown.append(lst[i])
      else:
        countdown = [lst[i]]
      if lst[i] == 1:
        countdown_lst += [countdown]
        count += 1
  return [count] + [countdown_lst]

