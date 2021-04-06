
def n_sided_shape(n):
 a={"circle":1,
    "semi-circle":2,
    "triangle":3,
    "square":4,
    "pentagon":5,
    "hexagon":6,
    "heptagon":7,
    "octagon":8,
    "nonagon":9,
    "decagon":10}
 b=dict(zip(a.values(),a.keys()))
 return b[n]

