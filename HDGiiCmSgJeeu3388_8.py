
def choose_fuse(fuses, current):
  
  fuse_nums = []
  
  for fuse in fuses:
    fuse = fuse.strip('V')
    fuse_nums.append(int(fuse))
  
  fuse_nums = sorted(fuse_nums)
  best_fuse = ''
  
  for num in fuse_nums:
    if num > float(current.strip('V')):
      best_fuse = str(num) + 'V'
      break
  if best_fuse == '':
    best_fuse = str(max(fuse_nums)) + 'V'
  return best_fuse

