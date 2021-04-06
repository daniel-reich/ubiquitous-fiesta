
def digital_clock(seconds):
​
  frmt = [(seconds // 3600) % 24, (seconds // 60) % 60, seconds % 60]
  result = ":".join([str(time) if time > 9 else "0" + str(time) for time in frmt])
  return result

