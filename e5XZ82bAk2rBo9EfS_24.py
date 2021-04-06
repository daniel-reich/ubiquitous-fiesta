
def bed_time(*times):
  time_diff_lst = []
  for x in times:
    alarm_time = int(x[0].replace(':', ''))
    time_to_sleep = int(x[1].replace(':', ''))
    time_diff_lst.append(time_to_sleep - alarm_time)
  final_lst = []
  for x in time_diff_lst:
    if x == 0:
      final_lst.append('00:00')
    elif x > 0:
      final_lst.append(str(2400 - x)[0:2] + ':' + str(2400 - x)[2:])
    else:
      final_lst.append('0' + str(x)[1] + ':' + str(x)[2:])
  return ['02:40' if x == '02:80' else x for x in final_lst]

