
limits = [5, 5, 10, 10, 15, 15, 20, 20]
def interview(lst, tot):
    return ("qualified" if tot <= 120 and len(lst) == 8 and
            all(v <= limits[i] for i, v in enumerate(lst)) else "disqualified")

