
def freed_prisoners(prison, first=True):
  if len(prison) == 0 or not any(prison) or (first and prison[0] == 0):
    return 0
  else:
    return 1 + freed_prisoners([1 - p for p in prison[prison.index(1)+1:]], False)

