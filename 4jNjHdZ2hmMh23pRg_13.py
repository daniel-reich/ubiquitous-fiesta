
def cutting_grass(lst, *cuts):
    x = []
    result = []
    for cut in cuts:
        for num in lst:
            x.append(num-cut)
        result.append(x)
        lst = x
        x = []
    r=[[0 if item <= 0 else item for item in row  ] for row in result]
    return ['Done' if 0 in row else row for row in r]

