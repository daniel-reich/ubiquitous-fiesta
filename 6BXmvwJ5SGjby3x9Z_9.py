
def hours_passed(time1, time2):
  def convert(time):
    lt = time.split()
    lt[0] = lt[0].replace(lt[0][-3:], '')
    for i in range(len(lt)):
      if lt[i].isdigit():
        if lt[i] == '12' and lt[i+1] == 'AM':
          lt[i] = 0
        else:
          lt[i] = int(lt[i])
      else:
        if lt[i] == 'AM':
          lt[i] = 0
        else:
          lt[i] = 12
    return lt
  tpassed = sum(convert(time2))-sum(convert(time1))
  return '{} hours'.format(tpassed) if not time1 == time2 else 'no time passed'

