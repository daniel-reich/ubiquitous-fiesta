
def pH_name(pH):
    if 0>pH or pH>14:
      return "invalid"
    if 0<pH<7:
      return "acidic"
    if 6.9<pH<8 :
      return "neutral"
    if 7<pH<14:
      return "alkaline"

