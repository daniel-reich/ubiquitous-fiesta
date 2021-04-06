
def BMI(weight, height):
    w_lst=weight.split()
    h_lst=height.split()
   # print(w_lst,' ',h_lst)
    if w_lst[1] == "pounds":
        kg=int(w_lst[0])*0.453592
    else: 
        kg=float(w_lst[0])
    if h_lst[1] == "inches":
        m=int(h_lst[0])*0.0254
    else:
        m=float(h_lst[0])
    bmi=round((kg/(m**2)),1)
    #print(bmi)
    if bmi < 18.5:
        output="Underweight"
    elif bmi < 24.9:
        output="Normal weight"
    elif bmi < 29.9:
        output="Overweight"
    else:
        output="Obesity"
    return str(bmi)+' '+output

