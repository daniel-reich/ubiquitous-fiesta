
import numpy as np
def chi_squared_test(data):
    row1=data.get("E")
    row2=data.get("T")
    rn1=[0,0]
    rn2=[0,0]
    totalr1=row1[0]+row1[1]
    totalr2=row2[0]+row2[1]
    totalc1=row1[0]+row2[0]
    totalc2=row1[1]+row2[1]
    total=row1[0]+row1[1]+row2[0]+row2[1]
    rn1[0]=(totalr1*totalc1)/total
    rn1[1]=(totalr1*totalc2)/total
    rn2[0]=(totalr2*totalc1)/total
    rn2[1]=(totalr2*totalc2)/total
    for i in range(2):
        rn1[i]=((row1[i]-rn1[i])**2)/rn1[i]
        rn2[i]=((row2[i]-rn2[i])**2)/rn2[i]
    sum=0
    sum=rn1[0]+rn1[1]+rn2[0]+rn2[1]
    if sum> 6.635:
        return [round(sum,1),"Edabitin effectiveness = 99%"]
    elif sum<6.635 and sum>3.841:
        return [round(sum,1),"Edabitin effectiveness = 95%"]
    elif sum<3.841:
        return [round(sum,1),"Edabitin is ininfluent"]

