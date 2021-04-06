
def BMR(p):
  cal = {1:1.2, 2:1.375, 3:1.55, 4:1.725, 5:1.9}
  if p["gender"]=="male":
    return round((66.47+(13.75*p["weight"])+(5.003*p["size"])-(6.755*p["age"]))*cal[p["sport"]],1)
  else:
    return round((655.1+(9.563*p["weight"]) + (1.85*p["size"])-(4.676*p["age"]))*cal[p["sport"]],1)

