
def pH_name(ph):
  
    return "acidic" if ph >0 and ph<=6.9999 else "alkaline" if ph>8.00001 and ph<14 else "neutral" if int(ph)==7 else "invalid" if ph<0 or ph>14 else None

