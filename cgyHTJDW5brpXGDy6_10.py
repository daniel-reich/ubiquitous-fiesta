
def hours_passed(start, end):
  convert = lambda r: [[int(k), 0][k == '12'] if k.isdigit()
            else [0, 12][k == 'PM'] for k in r.split(':00 ')]
  (s, x), (e, y) = convert(start), convert(end)
  return [str(e+y-s-x) + ' hours', 'no time passed'][start == end]

