
def foil(l):
  pi=3.1402
  fluidfoil=((0.0025*l/pi+4)**.5)*2
  ex=(fluidfoil)%0.0025
  realfoil=fluidfoil-ex+(0.0025 if ex else 0)
  return round(realfoil,4)

