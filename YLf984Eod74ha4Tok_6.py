
def leap_year(yr):
  return (not bool(yr % 4)) & (bool(yr % 100)) | (not bool(yr % 400))

