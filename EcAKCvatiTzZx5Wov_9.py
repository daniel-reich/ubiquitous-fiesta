
digits_dict={
"black":        0,
"brown":        1,
"red":          2,
"orange":       3,
"yellow":       4,
"green":        5,
"blue":         6,
"violet":       7,
"gray":         8,
"white":        9
}
magnitude_dict={
"black":        0,
"brown":        1,
"red":          2,
"orange":       3,
"yellow":       4,
"green":        5,
"blue":         6,
"violet":       7,
"gray":         8,
"white":        9,
"gold":         -1,
"silver":       -2
}
tolerance_dict={
"brown":   "+/-1%",
"red":     "+/-2%",
"green":   "+/-0.5%",
"blue":    "+/-0.25%",
"violet":  "+/-0.1%",
"gray":    "+/-0.05%",
"gold":    "+/-5%",
"silver":  "+/-10%"
}
tcr_dict={
"brown":    "100ppm/k",
"red":      "50ppm/k",
"orange":   "15ppm/k",
"yellow":   "25ppm/k",
"blue":     "10ppm/k",
"violet":   "5ppm/k"
}
​
def resistor_code(l):
    if len(l)==4:
        rv=digits_dict[l[0]]*10+digits_dict[l[1]]
        rv*=10**(magnitude_dict[l[2]])
        tol=tolerance_dict[l[3]]
        tcr=''
    elif len(l)==5 or len(l)==6:
        rv=digits_dict[l[0]]*100+digits_dict[l[1]]*10+digits_dict[l[2]]
        rv*=10**(magnitude_dict[l[3]])
        tol=tolerance_dict[l[4]]
        tcr=tcr_dict[l[5]] if len(l)==6 else ''
    if rv>=1e9:
        rvs=str(rv/1e9 if int(rv/1e9)!=rv/1e9 else int(rv/1e9))
        rvs=rvs+'GOhm'
    elif rv>=1e6:
        rvs=str(rv/1e6 if int(rv/1e6)!=rv/1e6 else int(rv/1e6))
        rvs=rvs+'MOhm'
    elif rv>=1e3:
        rvs=str(rv/1e3 if int(rv/1e3)!=rv/1e3 else int(rv/1e3))
        rvs=rvs+'kOhm'
    else:
        rvs=str(rv)+'Ohm'
    if len(l)>5:
        return rvs+' '+tol+' '+tcr
    else:
        return rvs+' '+tol

