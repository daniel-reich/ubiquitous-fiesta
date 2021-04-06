
def slicer(s, slice_part):
  if len(slice_part) == 1 :
    return "[{}]".format(s.index(slice_part))
  indices  = [s.index(e) for e in slice_part]
  step  = [ right  - left for left,right in zip(indices , indices[1:])][0]
  direction  = 1 if step > 0 else -1
  
  display_begin  = "{}".format(indices[0]) if len(s)-1 > indices[0] > 0 else ""
  display_end  = "{}".format(indices[-1]+direction) if len(s) > indices[-1]+step > -1 else ""
  display_step = "{}".format(step) if step != 1 else ""
  display = "{}:{}:{}".format(display_begin , display_end , display_step ).rstrip(":")
  return  "[{}]".format(display if display else ":")

