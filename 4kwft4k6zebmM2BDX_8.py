
def chi_squared_test(data):
    orig_e2 = data["E"][0]
    orig_e30 = data["E"][1]
    orig_t2 = data["T"][0]
    orig_t30 = data["T"][1]
    
    e_row_total = data["E"][0] + data["E"][1]
    t_row_total = data["T"][0] + data["T"][1]
    a2h_total = data["E"][0] + data["T"][0]
    a30min_total = data["E"][1] + data["T"][1]
    overall_total = e_row_total + t_row_total
    
    estimated_e2 = (e_row_total * a2h_total)/overall_total
    estimated_e30 = (e_row_total * a30min_total)/overall_total
    estimated_t2 = (t_row_total * a2h_total)/overall_total
    estimated_t30 = (t_row_total * a30min_total)/overall_total
    
    new_e2 = ((orig_e2-estimated_e2)**2)/estimated_e2
    new_e30 = ((orig_e30-estimated_e30)**2)/estimated_e30
    new_t2 = ((orig_t2-estimated_t2)**2)/estimated_t2
    new_t30 = ((orig_t30-estimated_t30)**2)/estimated_t30
​
    chi_squared = new_e2 + new_e30 + new_t2 + new_t30
​
    if chi_squared > 6.635:
        return [round(chi_squared,1), "Edabitin effectiveness = 99%"]
    elif chi_squared > 3.831:
        return [round(chi_squared, 1), "Edabitin effectiveness = 95%"]
    else:
        return [round(chi_squared, 1), "Edabitin is ininfluent"]

