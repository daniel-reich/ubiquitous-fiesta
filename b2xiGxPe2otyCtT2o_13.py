
def how_many_times(msg):
  return 0 if not msg else ord(msg[0])-ord('a')+1+how_many_times(msg[1:])

