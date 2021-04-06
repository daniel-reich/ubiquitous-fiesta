
def BMR(person):
​
    if person["gender"] == "male":
        bmr_val = 66.47 + (13.75 * person["weight"]) + (5.003 * person["size"]) - (6.755 * person["age"])
​
    elif person["gender"] == "female":
        bmr_val = 655.1 + (9.563 * person["weight"]) + (1.85 * person["size"]) - (4.676 * person["age"])
​
    if person["sport"] == 1:
        new_val = bmr_val * 1.2
    elif person["sport"] == 2:
        new_val = bmr_val * 1.375
    elif person["sport"] == 3:
        new_val = bmr_val * 1.55
    elif person["sport"] == 4:
        new_val = bmr_val * 1.725
    elif person["sport"] == 5:
        new_val = bmr_val * 1.9
​
    a = round(new_val, 1)
    return a

