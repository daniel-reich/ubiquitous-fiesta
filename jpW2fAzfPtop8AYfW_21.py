
def to_dict(liste):
    return [{i:ord(i)} for i in liste] if len(liste)>0 else liste

