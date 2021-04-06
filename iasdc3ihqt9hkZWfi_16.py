
def can_give_blood(donor, receiver):
    if donor=="O-": return True
    elif donor=="O+" and receiver[-1]=="+": return True
    elif donor=="A-" and receiver[0]=="A": return True
    elif donor=="A+" and receiver[0]=="A" and receiver[-1]=="+": return True
    elif donor=="B-" and "B" in receiver: return True
    elif donor=="B+" and "B+" in receiver: return True
    elif donor=="AB-" and "AB" in receiver: return True
    elif donor=="AB+" and receiver=="AB+": return True
    return False

