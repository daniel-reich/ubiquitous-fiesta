
def freed_prisoners(prison):
  lock = 1
  freed = 0
  if prison[0] == 0:
    return 0
  for i in prison:
    if i == lock:
      freed += 1
      lock = (lock + 1) % 2
  return freed

