
def calculate_score(lst):
    a =0
    b =0
    for ab,be in lst:
        if ab=='R':
            if be == 'P':
                b+=1
            if be == 'S':
                a+=1
        if ab == "P":
            if be =='S':
                b+=1
            if be =="R":
                a+=1
        if ab == 'S':
            if be == 'R':
                b+=1
            if be == 'P':
                a+=1
    if a>b:
        return "Abigail"
    if b>a:
        return "Benson"
    if a==b:
        return "Tie"

