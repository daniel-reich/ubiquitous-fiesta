
is_shape_possible = lambda n, a: (n-2)*180 == sum(x for x in a) \
    and n > 2 and all(x in range(1, 180) for x in a)

