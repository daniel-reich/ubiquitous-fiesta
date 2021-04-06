
def kix_code(addr):
  ans = ''.join([addr.split(',')[2].split()[i] for i in [0,1]])
  if not addr.split(',')[1].split()[-1][0].isdigit():
    ans+=('X'.join(addr.split(',')[1].split()[-2:]))
  else:
    ans+=(addr.split(',')[1].split()[-1].replace('-','X').replace('/','X'))
  return ans.upper()

