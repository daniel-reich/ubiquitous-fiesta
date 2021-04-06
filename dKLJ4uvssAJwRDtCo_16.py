
def vending_machine(products, money, product_number):
  price = 0
  name = ""
  clst = [500, 200, 100, 50, 20, 10]
  for i in products:
    if i["number"] == product_number:
      price = i["price"]
      name = i["name"]
  if money-price<0:
    return "Not enough money for this product"
  change = money-price
  if price == 0:
    return "Enter a valid product number"
  val = change
  lst=[]
  switch = True
  for i in clst:
    if switch == False:
       break
    if val>=i:
      if val%i == 0:
        count = int(val/i)
        for b in range(count):
          lst.append(i)
          add = 0
          for c in lst:
            add = c+add
          if add == change:
            switch = False
            break
      else:
        val = change-i
        lst.append(i)
  dict1 = {"product":name,"change":lst}
  return dict1

