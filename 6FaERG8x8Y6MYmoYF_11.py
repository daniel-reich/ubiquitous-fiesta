
def dice_score(throw):
    # throw=sorted(throw)
    d_score = 0
    for number in throw:
        if 1 in throw:
            if throw.count(1)<3:
                d_score += 100*throw.count(1)
            elif throw.count(1)==3:
                d_score += 1000
            elif throw.count(1)==4:
                d_score +=1000+(4*100)
            else:
                d_score += 1200
        if 6 in throw:
            if throw.count(6)==3:
                d_score += 600
        if 5 in throw:
            if throw.count(5)<3:
                d_score += 50*throw.count(5)
            elif throw.count(5)==3:
                d_score += 500
        if 4 in throw:
            if throw.count(4)==3:
                d_score += 400
        if 3 in throw:
            if throw.count(3)==3:
                d_score += 300
        if 2 in throw:
            if throw.count(2)==3:
                d_score += 200
​
        return d_score

