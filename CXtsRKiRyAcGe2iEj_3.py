
def time_to_finish(full, part):
  
  char_time = .5
  char_diff = len(full.replace(' ','')) - len(part.replace(' ', '')) 
  
  return char_diff * char_time

