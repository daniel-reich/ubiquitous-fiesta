
def find_vertex(x):
    x = x.replace(" ", "")
    loc_a = x.find("x")
    loc_b = x.find("x", loc_a+1)
    a = int(x[:loc_a])
    b = int(x[loc_a+1:loc_b])
    return round(-b//(2*a), 0)

