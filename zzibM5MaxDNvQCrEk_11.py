
def will_fit(holds, cargo):
    new = [50 if i == "S" else 100 if i == "M" else 200 for i in holds]
    if sum(new) < sum(cargo):
        return False
    else:
        return True

