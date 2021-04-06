
def chemical_reactions(C, H, O):
  W=min(divmod(H,2)[0],O)
  H=divmod(H,2)[1] if W else H
  O=O-W if O>=W else O
  CO=min(divmod(O,2)[0],C)
  C=C-CO if C>=CO else C
  CH=min(divmod(H,4)[0], C)
  return [W, CO, CH]

