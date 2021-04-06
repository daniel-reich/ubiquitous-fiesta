
def security(txt):
    thief=False
    money=False
    guard=False
    if txt[-3::]=='TTT':
        return "Safe"
    for i in txt:
        if i=='$':
            money=True
            if thief and not guard:
                return 'ALARM!'
            guard=False
        if i=="T":
            thief=True
            if money and not guard:
                return 'ALARM!'
            guard=False
        if i=='G':
            guard=True
            if thief:
                thief=False
    return "Safe"

