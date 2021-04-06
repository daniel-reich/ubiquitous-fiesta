
def chemical_reactions(c, h, o):
  H2o=min([h//2,o])
  Co2=min([c,(o-H2o)//2])
  Ch4=min([c-Co2,(h-2*H2o)//4])
  return [H2o, Co2, Ch4]

