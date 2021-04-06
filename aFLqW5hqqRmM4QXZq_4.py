
def bar_chart(sales):
  sales_reverse = {sales[i]:i for i in sales}
  sales_value_list = []
  
  for e in sales:
    if len(sales_value_list) == 0:
      sales_value_list.append(e)
    else:
      insert = False
      for i in range(len(sales_value_list)):
        if sales[e] > sales[sales_value_list[i]] or (sales[e] == sales[sales_value_list[i]] and e < sales_value_list[i]):
          sales_value_list.insert(i,e)
          insert = True
          break
      if insert == False:
        sales_value_list.append(e)
          
  result = ""
  for i,e in enumerate(sales_value_list):
    count = sales[e]//50
    if count == 0:
      result += (e + "|" + "0")
    else:
      result += (e + "|" + "#"*count + " "+ str(sales[e]))
    if i != 3:
      result += "\n"
  
  return result

