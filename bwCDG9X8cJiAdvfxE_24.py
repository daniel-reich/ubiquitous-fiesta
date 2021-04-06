
def add_str_nums(n1, n2):
    try:
        return str(int(n1)+int(n2))
    except:
        if n1 == "" and n2 == "": return "0"
        if n1 == "": return n2
        if n2 == "": return n1
        else:
            return "-1"

