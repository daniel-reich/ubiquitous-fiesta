
def logarithm(base, num):
  if base <= 1 or num <= 0:
    return "Invalid"
  log = 0
  while num != 1:
    num /= base
    log += 1
  return log

