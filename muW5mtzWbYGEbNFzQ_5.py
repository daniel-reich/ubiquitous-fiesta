
def BMR(person): 
    s = [1.2,1.375,1.55,1.725,1.9]
    if person["gender"] == "male":
        return round((66.47+(13.75*person["weight"])+(5.003*person["size"])-(6.755*person["age"]))*s[person["sport"]-1],1)
    else:
        return round((655.1 + (9.563 * person["weight"]) + (1.85 * person["size"]) - (4.676 * person["age"]))*s[person["sport"]-1],1)

