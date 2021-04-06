
def digital_clock(seconds):
  min, sec = divmod(seconds, 60) 
  hour, min = divmod(min, 60) 
  return "%02d:%02d:%02d" % (hour if hour<24 else hour%24 , min, sec)

