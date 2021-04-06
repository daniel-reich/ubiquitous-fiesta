
def perimeter(lst):
    return round(
        sum(
            (
                distance(lst[0], lst[1]),
                distance(lst[1], lst[2]),
                distance(lst[2], lst[0]),
            )
        ),
        2,
    )
​
def distance(p, q):
    return ((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2) ** 0.5

