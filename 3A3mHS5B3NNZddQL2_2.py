
def interview(lst, tot):
    if len(lst)<8 or tot>120: return "disqualified"
    for t,l in zip(lst,[5,5,10,10,15,15,20,20]):
        if t>l: return "disqualified"
    return 'qualified'

