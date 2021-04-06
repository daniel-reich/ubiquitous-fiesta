
def minutes_to_seconds(time):
  minutes, seconds = [int(i) for i in time.split(':')]
  return False if seconds > 59 else minutes * 60 + seconds

