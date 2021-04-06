
def ping_pong(lst, win):
  totHits = len(lst * 2)
  if not win:
    totHits -= 1
  return ["Pong!" if i % 2 else "Ping!" for i in range(totHits)]

