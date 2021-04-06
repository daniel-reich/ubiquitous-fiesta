
def temp_conversion(cel):
  return [round(9*cel/5+32,2) ,round(cel+273.15,2)] if cel>=-273.15 else "Invalid"

