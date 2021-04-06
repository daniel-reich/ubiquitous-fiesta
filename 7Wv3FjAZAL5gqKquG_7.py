
def era(er, ip):
  
  IP_String = str(ip)
  
  if ("." in IP_String):
    Components = IP_String.split(".")
    Full_Outs = int(Components[0]) * 3
    Part_Outs = int(Components[1]) * 1
    Outs = Full_Outs + Part_Outs
    
  else:
    Outs = int(IP_String) * 3
  
  ERA = (er / Outs) * 27
  ERA = round(ERA,2)
  
  Answer = "{:.2f}".format(ERA)
  
  return Answer

