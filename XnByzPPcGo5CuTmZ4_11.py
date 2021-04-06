
def kix_code(addr):
  addr=''.join(' ' if not c.isalnum() else c for c in addr).split()
  for i in range(len(addr)):
    if len(addr[i])==4 and addr[i].isdigit() and len(addr[i+1])==2 and addr[i+1].isupper():
      return addr[i]+addr[i+1]+(addr[i-2]+'X'+addr[i-1] if addr[i-2].isdigit() else addr[i-1]).upper()

