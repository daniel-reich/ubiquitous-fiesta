
def p_area(lst):
    area = 0
    j = len(lst) - 1
    for i, v in enumerate(lst):
        area += (lst[j][0] + v[0]) * (lst[j][1] - v[1])
        j = i
    return area / 2
​
​
def which_side(poly, vert):
    a = p_area(poly)
    if a < 0:
        a *= -1
        poly = poly[::-1]
    poly_1 = [tpl for tpl in poly if tpl != vert]
    a1 = p_area(poly_1)
    return 'regular' if a1 < a else 'reflex'

