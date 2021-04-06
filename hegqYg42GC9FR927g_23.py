
def amazing_edabit(s):
    if "edabit" in s:
        return s
    else:
        if "amazing" in s:
            s = s.replace("amazing", "not amazing")
            return s

