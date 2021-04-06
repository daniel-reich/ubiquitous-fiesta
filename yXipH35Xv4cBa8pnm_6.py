
def microwave_buttons(t):
  (m, s) = t.split(':')
  if int(m) * 60 + int(s) < 30 and int(m) * 60 + int(s) > 0 : return 3
  elif int(m) * 60  + int(s) == 0: return 1
  elif int(m) * 60 + int(s) >= 600: return 5
  elif int(s) > 60: return 3
  else: return(int(m) * 60 + int(s)) / 30 + 1

