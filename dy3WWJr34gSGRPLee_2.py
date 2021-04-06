
def make_box(n):
    a = []
    for i in range(n):
        if i == (n-1) or i == 0: 
            a.append(n*"#")
        else:
            a.append("#" + (n-2)*(" ")+ "#")
    return a

