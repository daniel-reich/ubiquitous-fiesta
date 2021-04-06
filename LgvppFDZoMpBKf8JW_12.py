
def digital_clock(seconds):
  h = ("0" * (seconds<(10*3600) or seconds>(24*3600)))+str((seconds//3600)%24)
  m = ("0" * (seconds//60%60<10)) + str(seconds//60%60)
  s = ("0" * (seconds%60 < 10)) + str(seconds%60)
  return ":".join([h,m,s])

