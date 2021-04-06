
def security(monitor):
    theft,cash = False, False
    for state in monitor:
        if state == "T":
            theft = True
        elif state == "G":
            theft = False
            cash = False
        elif state == "$":
            cash = True
        if theft and cash:
            return "ALARM!"
    return "Safe"

