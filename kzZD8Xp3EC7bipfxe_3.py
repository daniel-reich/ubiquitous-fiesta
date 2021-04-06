
def worded_math(equ):
    d = {"zero":0,"one":1,"two":2,"three":3,"four":4,"five":5,"six":6,"seven":7,"eight":8,"nine":9,"plus":"+","minus":"-"}
    value = eval("".join([str(d[e.lower()]) for e in equ.split() ]))
    vw = list(d.keys())[list(d.values()).index(value)]
    return vw[0].upper()+vw[1:]

