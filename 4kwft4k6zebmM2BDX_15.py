
def chi_squared_test(data):
 alpha1 = 6.635
 alpha5 = 3.841
​
 statement1 = "Edabitin effectiveness = 99%"
 statement2 = "Edabitin effectiveness = 95%"
 statement3 = "Edabitin is ininfluent"
​
 sum_total = 0
​
 for x,y in data.items():
     for i in y:
         sum_total = sum_total + i
​
 sum_edabitin_row = 0
 sum_tutorial_row = 0
 sum_twohrs_column = 0
 sum_halfhrs_column = 0
​
 edabitin_row = [y for x,y in data.items() if "E" in x]
​
 edabitin_row = [j for i in edabitin_row for j in i]
​
 for x in edabitin_row:
     sum_edabitin_row = sum_edabitin_row + x
​
 tutorial_row = [y for x,y in data.items() if "T" in x]
 tutorial_row = [y for x in tutorial_row for y in x]
​
 for x in tutorial_row:
     sum_tutorial_row = sum_tutorial_row + x
​
 twohrs_column = [y[0] for x,y in data.items()]
​
 for x in twohrs_column:
     sum_twohrs_column = sum_twohrs_column + x
​
 halfhrs_column = [y[1] for x,y in data.items()]
​
 for y in halfhrs_column:
     sum_halfhrs_column = sum_halfhrs_column + y
​
​
 edabitin_twohrs_cell = (sum_edabitin_row * sum_twohrs_column) / sum_total
 edabitin_halfhrs_cell = (sum_edabitin_row * sum_halfhrs_column) / sum_total
 tutorial_twohrs_cell = (sum_tutorial_row * sum_twohrs_column) / sum_total
 tutorial_halfhrs_cell = (sum_tutorial_row * sum_halfhrs_column) /sum_total
​
 data['E'][0] = (data['E'][0] - edabitin_twohrs_cell)**2 / edabitin_twohrs_cell
 data['E'][1] = (data['E'][1] - edabitin_halfhrs_cell)**2 / edabitin_halfhrs_cell
 data['T'][0] = (data['T'][0] - tutorial_twohrs_cell)**2 / tutorial_twohrs_cell
 data['T'][1] = (data['T'][1] - tutorial_halfhrs_cell)**2 / tutorial_halfhrs_cell
​
 list1 = []
​
 for x,y in data.items():
     for i in y:
         list1.append(i)
 list1 = sum(list1)
 list1 = round(list1,1)
​
 result1 = [list1, statement1]
 result2 = [list1, statement2]
 result3 = [list1, statement3]
​
 if list1 > alpha1:
     return result1
 elif list1 < alpha1 and list1 > alpha5:
     return result2
 else:
     return result3
​
print(chi_squared_test({"E": [90, 50], "T": [80, 40]}))

