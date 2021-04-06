
def time_adjust(now, hrs, mins, sec):
  now = [int(i) for i in now.split(":")]
  now[2] += sec % 60
  mins += sec // 60
  now[1] += mins % 60
  hrs += mins // 60
  if now[2] > 59:
    now[1] += 1
    now[2] = now[2] % 60
  if now[1] > 59:
    now[0] += 1
    now[1] = now[1] % 60
  now[0] = (now[0] + hrs) % 24
  now = ["0" + str(i) if i < 10 else str(i) for i in now ]
  return "{}:{}:{}".format(now[0], now[1], now[2])

