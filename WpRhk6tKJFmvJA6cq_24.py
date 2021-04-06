
def manage_delays(train, dest, delay):
  if (dest in train.destinations):
    et_dest = train.expected_time
    et_dest = et_dest.split(':')
    et_dest = [int(i) for i in et_dest]
    et_dest[1] += delay%60
    if et_dest[1] > 60:
      et_dest[1] -= 60
      et_dest[0] += 1
    et_dest[0] += delay//60
    et_dest = [str(i) for i in et_dest]
    if len(et_dest[0]) == 1: et_dest[0] = '0' + et_dest[0]
    if len(et_dest[1]) == 1: et_dest[1] = '0' + et_dest[1]
    train.expected_time = ':'.join(et_dest)

