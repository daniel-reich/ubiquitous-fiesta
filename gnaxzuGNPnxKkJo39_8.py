
from math import floor
def easter_date(year):
  a, b, c = year % 19, year % 4, year % 7
  k = floor(year / 100)
  p, q = floor((13 + 8 * k) / 25), floor(k / 4)
  M, N = (15 - p + k - q) % 30, (4 + k - q) % 7
  d = (19 * a + M) % 30
  e = (2 * b + 4 * c + 6 * d + N) % 7
  mar = 22 + d + e
  apr = d + e - 9
  return 'March ' + str(mar) if 22 <= mar <= 31 else "April " + str(apr)

