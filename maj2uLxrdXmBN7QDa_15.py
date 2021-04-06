
def bishop(start, end, n):
    # Translation letters to numbers : a=>1, b=>2 , c=>3 ...
    case1 = start.translate(str.maketrans('abcdefgh', '12345678'))
    case2 = end.translate(str.maketrans('abcdefgh', '12345678'))
    # Check if the begin and the end are in the same color
    color = lambda position : "Black" if int(position[0])%2 == int(position[1])%2 else "White"
    if color(case1) != color(case2):
        return False
    if case1 == case2:
        return True
    if case2[0] != case1[0] :
        m = (int(case2[1]) - int(case1[1])) / (int(case2[0]) - int(case1[0]))
    else :
        m=0
    if n==1 and m in [ 1 , -1 ]:
        return True
    if n > 1:
        return True
    return False

