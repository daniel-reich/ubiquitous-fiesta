
tax = .06
def checkout(cart):
  
  # Putting Dictionary Properties into Lists
  
  Prices = []
  Quantities = []
  Tax_Status = []
  
  Counter = 0
  Length = len(cart)
  
  while (Counter < Length):
  
    Item = cart[Counter]
    
    Prices.append(Item["prc"])
    Quantities.append(Item["qty"])
    Tax_Status.append(Item["taxable"])
    
    Counter += 1
  
  # Building Total
  
  Total_Outlay = 0
  
  Counter = 0
  Length = len(Tax_Status)
  
  while (Counter < Length):
    
    Pre_Tax = Prices[Counter] * Quantities[Counter]
    Taxable = Tax_Status[Counter]
    
    if (Taxable == True):
      Post_Tax = Pre_Tax * 1.06
      Total_Outlay += Post_Tax
      Counter += 1
    else:
      Post_Tax = Pre_Tax * 1.00
      Total_Outlay += Post_Tax
      Counter += 1
  
  return Total_Outlay

