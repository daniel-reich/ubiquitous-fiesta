
def sle (list1):
    equation1 = list1[0]
    equation2 = list1[1]
    a , b , c = equation1[0]  , equation1[1]   , equation1[2]
    d , e , f = equation2[0]  , equation2[1]   , equation2[2]
    denom = a * e - b * d
    if  denom == 0:
        return False
    return (  int((c*e - b*f)/denom), int((a*f - c*d)/denom) )

