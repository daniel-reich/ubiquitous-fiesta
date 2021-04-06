
def resistor_code(colors):
    d = {
    "black" : [0,0,"",""],
    "brown":[1,1,"+/-1%","100ppm/k"],
    "red":[2,2,"+/-2%","50ppm/k"],
    "orange":[3,3,"","15ppm/k"],
    "yellow":[4,4,"","25ppm/k"],
    "green":[5,5,"+/-0.5%",""],
    "blue":[6,6,"+/-0.25%","10ppm/k"],
    "violet":[7,7,"+/-0.1%","5ppm/k"],
    "gray":[8,8,"+/-0.05%",""],
    "white":[9,9,"",""],
    "gold":["",-1,"+/-5%",""],
    "silver":["",-2,"+/-10%",""]  
    }
    
    if len(colors) == 4:
        r4 = int(str(d[colors[0]][0]) + str(d[colors[1]][0]))    
        m4 = 10 ** (int(d[colors[2]][1]))
        rm4 = r4 * m4
        if rm4 % 10**9 == 0:
            rm44 = rm4 // (10**9)
            p = "G"
        elif rm4 % 10**6 == 0:
            rm44 = rm4 // (10**6)
            p = "M"
        elif rm4 > 1000:
            rm44 = rm4 / (10**3)
            p = "k"
        else:
            rm44 = rm4
            p = "OM"
        return (str(rm44) + p + "Ohm" + " " +d[colors[3]][2])
            
    if len(colors) == 5:
        r5 = int(str(d[colors[0]][0]) + str(d[colors[1]][0]) + str(d[colors[2]][0]))           
        m5 = 10 ** (int((d[colors[3]][1])))    
        rm5 = r5 * m5
        if rm5 % 10**9 == 0:
            rm55 = rm5 // (10**9)
            p = "G"
        elif rm5 % 10**6 == 0:
            rm55 = rm5 // (10**6)
            p = "M"
        elif rm5 >  1000:
            rm55 = rm5 // (10**3)
            p = "k"
        else:
            rm55 = rm5
            p = ""
        return (str(rm55) + p + "Ohm"+ " "  +d[colors[4]][2])            
    
    if len(colors) == 6:
        r6 = int(str(d[colors[0]][0]) + str(d[colors[1]][0]) + str(d[colors[2]][0]))         
        m6 = 10 ** (int(d[colors[3]][1]))
        rm6 = r6 * m6
        if rm6 % 10**9 == 0:
            rm66 = rm6 // (10**9)
            p = "G"
        elif rm6 % 10**6 == 0:
            rm66 = rm6 // (10**6)
            p = "M"
        elif rm6 >  1000:
            rm66 = rm6 // (10**3)
            p = "k"
        else:
            rm66 = rm6
            p = ""
        return (str(rm66) + p + "Ohm" + " " + d[colors[4]][2] + " " + d[colors[5]][3])

