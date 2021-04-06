
def verbify(txt):
  return txt if txt.split()[0][-2:]=='ed' else txt.split()[0]+'d'+' '+txt.split()[1] if txt.split()[0][-1]=='e' else txt.split()[0]+'ed'+' '+txt.split()[1]

