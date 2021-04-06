
def format_phone_number(lst):
    lst = [str(i) for i in lst]
    return "("+"".join(lst[:3])+")" + " " + "".join(lst[3:6]) + "-" + "".join(lst[6:])

