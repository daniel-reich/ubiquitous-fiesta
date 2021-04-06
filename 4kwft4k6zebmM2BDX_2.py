
def chi_squared_test(data):
  def step_1(eda_2hr, eda_half, tut_2hr, tut_half):
    row_total = [eda_2hr + eda_half, tut_2hr + tut_half]
    col_total = [eda_2hr + tut_2hr, eda_half + tut_half]
    total = eda_2hr + tut_2hr + eda_half + tut_half
​
    return [row_total, col_total, total]
  def step_2(s1):
    
    eda = int(s1[0][0])
    tut = int(s1[0][1])
    
    thrs = int(s1[1][0])
    hhrs = int(s1[1][1])
​
    total = int(s1[2])
​
    cell1 = (eda * thrs) / total
    cell2 = (eda * hhrs) / total
    cell3 = (tut * thrs) / total
    cell4 = (tut * hhrs) / total
​
    return [cell1, cell2, cell3, cell4]
  def step_3(s2, eda2, edahalf, tut2, tuthalf):
    
    cell1 = s2[0]
    cell2 = s2[1]
    cell3 = s2[2]
    cell4 = s2[3]
​
    newc1 = (eda2 - cell1)**2 / cell1
    newc2 = (edahalf - cell2)**2/cell2
    newc3 = (tut2 - cell3)**2/cell3
    newc4 = (tuthalf - cell4)**2/cell4
​
    return newc1, newc2, newc3, newc4
  def step_4(cells):
​
    cell1 = cells[0]
    cell2 = cells[1]
    cell3 = cells[2]
    cell4 = cells[3]
​
    s = cell1 + cell2 + cell3 + cell4
​
    s = round(s, 1)
​
    return s
  def step_5(chi_rating):
    
    alpha1 = 6.635
    alpha5 = 3.841
​
    percentages = {'alpha1': 99, 'alpha5': 95}
​
    alpha = ''
​
    if chi_rating > alpha1:
      alpha = 'alpha1'
    elif chi_rating < alpha1 and chi_rating > alpha5:
      alpha = 'alpha5'
    else:
      return "Edabitin is ininfluent"
​
    percent = percentages[alpha]
​
    tr = 'Edabitin effectiveness = {p}%'.format(p = percent)
​
    return tr 
​
  edabitin = data['E']
  
  eda_2hr = int(edabitin[0])
  eda_halfhr = int(edabitin[1])
​
  tutorial = data['T']
​
  tut_2hr = int(tutorial[0])
  tut_halfhr = int(tutorial[1])
​
  s1 = step_1(eda_2hr, eda_halfhr, tut_2hr, tut_halfhr)
  s2 = step_2(s1)
  s3 = step_3(s2, eda_2hr, eda_halfhr, tut_2hr, tut_halfhr)
  s4 = step_4(s3)
  s5 = step_5(s4)
​
  return [s4, s5]

