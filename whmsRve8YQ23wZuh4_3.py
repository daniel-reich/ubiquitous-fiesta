
def sort_dates(lst, mode):
  def key(s):
    date, time = s.split('_')
    d, m, y = map(int,date.split('-'))
    h, minute = map(int,time.split(':'))
    return (y, m, d, h, minute)
  return sorted(lst, key=key, reverse=(mode=='DSC'))

