
def is_curzon(num):
  return True if (2 ** num + 1) % (2 * num + 1) == 0 else False

