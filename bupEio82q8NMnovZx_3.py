
def track_robot(instructions):
  insts = [inst.split(" ") for inst in instructions]
  mov = {}
  for key, val in insts:
    mov[key] = mov.get(key, 0) + int(val)
  return [mov.get('right', 0) - mov.get('left', 0), 
      mov.get('up', 0) - mov.get('down', 0)]

