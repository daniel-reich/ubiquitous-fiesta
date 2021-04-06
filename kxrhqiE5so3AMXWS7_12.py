
def get_number_of_apples(n, p):
    if len(p) == 3:
        res_str = p[:2] + p[3:]
    elif len(p) == 4:
        res_str = p[:3] + p[4:]
    children_get = n - (n * 0.01 * int(res_str))
    if n > 0 and res_str != "100":
        return children_get - (children_get % 1)
    if n <= 0 or res_str == "100":
        return "The children didn't get any apples"

