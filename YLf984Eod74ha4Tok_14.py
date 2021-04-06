
def leap_year(yr):
   code = 4*(yr % 400 == 0) + 2*(yr % 100 == 0) + (yr % 4 == 0)
   return code in (1, 7)

