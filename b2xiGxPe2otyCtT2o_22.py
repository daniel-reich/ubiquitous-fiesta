
import string
def how_many_times(msg):
  return sum([list(string.ascii_lowercase).index(i)+1 for i in msg])

