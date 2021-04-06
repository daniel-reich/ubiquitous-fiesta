
def microwave_buttons(time):
  minutes, seconds = time.split(':')
  total_time = (int(minutes) * 60) + int(seconds)
  presses_with_30_second_buttton = total_time // 30
  presses_with_number_buttons = 4
  for character in time:
    if character == '0':
      presses_with_number_buttons = presses_with_number_buttons - 1
    elif character == ':':
      continue
    else:
      break
  if presses_with_30_second_buttton * 30 != total_time:
    return presses_with_number_buttons + 1
  else:
    return min(presses_with_30_second_buttton, presses_with_number_buttons) + 1

