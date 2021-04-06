
def counter() -> int:
  if not hasattr(counter, 'count'):
    counter.count = 0
  counter.count += 1
  return counter.count - 1

