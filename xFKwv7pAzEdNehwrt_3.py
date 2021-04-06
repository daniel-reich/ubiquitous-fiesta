
def bracket_logic(xp):
    new = ""
    for c in xp:
        if c in "{[(<>)}]":
            new += c
​
    if (len(new) % 2) == 0:
        i = 0
        while i <= len(new):
            new = new.replace("()", "")
            new = new.replace("<>", "")
            new = new.replace("{}", "")
            new = new.replace("[]", "")
            i += 1
        if len(new) == 0:
            return True
    return False

