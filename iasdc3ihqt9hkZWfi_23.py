
def can_give_blood(donor, receiver):
    if donor=="O-":
        return True
    elif receiver=="AB+":
        return True
    elif donor=="O+":
        return receiver[-1:]=="+"
    elif donor==receiver:
        return True
    else:
        return False

