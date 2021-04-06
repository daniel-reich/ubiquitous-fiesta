
def alpha_range(start, stop, *interval):
  string = "abcdefghijklmnopqrstuvwxyz"
  if bool(start.isupper()) != (stop.isupper()):
    return "both start and stop must share the same case"
  if start.isupper():
    string = string.upper()
  ind_1,ind_2 = string.index(start),string.index(stop)
  begin,end = min(ind_1,ind_2),max(ind_1,ind_2)
  step = 1
  if len(interval) == 1:
    step = interval[0]
  if abs(step) > 26 or step == 0:
    return "step must be a non-zero value between -26 and 26, exclusive"
  if step < 0:
    begin,end = end,begin
    if end == 0:
      return [x for x in string[begin::step]]
    end -=1 
  else:
    end +=1
  return [x for x in string[begin:end:step]]

