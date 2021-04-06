
def temp_conversion(celsius):
  conv_List = [celsius*9/5 +32, celsius+273.15]
  return [round(i, 2) for i in conv_List] if conv_List[1] > 0 else "Invalid"

