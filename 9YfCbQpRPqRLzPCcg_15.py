
def will_hit(formula,coordinate):
    formula_list = formula.split(" ")
    x_multi = formula_list[-3]
    digit = []
    
    
    #compute x
    if x_multi[0] == "-":
        for charac in range(1,(len(formula_list[-3])-1)):
            digit.append(x_multi[charac])
            final_x = float("".join(digit)) * -1 * coordinate[0]
    if x_multi[0] != "-":
        for charac in range(0,(len(formula_list[-3])-1)):
            digit.append(x_multi[charac])
            final_x = float("".join(digit)) * 1 * coordinate[0]
    
    
    #compute y
    if formula_list[-2] == "-":
        y_multi = -1 * float(formula_list[-1])
    
    if formula_list[-2] == "+":
        y_multi = 1 * float(formula_list[-1])
        
    if y_multi + final_x == coordinate[1]:
        return True
    else:
        return False
    
    return formula_list

