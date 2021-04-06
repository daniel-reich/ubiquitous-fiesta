
def percentage_changed(old, new):
    old = int(old[1:])
    new = int(new[1:])
    present = round((old - new) / old * 100)
    return str(present) + "% decrease" if present > 0 else str(-present) + "% increase"

