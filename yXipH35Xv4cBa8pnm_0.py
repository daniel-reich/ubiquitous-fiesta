
def microwave_buttons(time):
  try:
    return ('00:00', '00:30', '01:00').index(time) + 1
  except:
    return len(time.lstrip('0'))

