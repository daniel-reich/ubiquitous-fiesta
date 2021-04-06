
def vending_machine(products,money,product_number):
   if product_number<=0 or product_number>=10: return 'Enter a valid product number'
   def chmon(mon,lst=[]):
     change = [500, 200, 100, 50, 20, 10]
     n=0
     while n in range(len(change)):
       lst.append(change[n])
       if sum(lst)==mon:
           return lst
       elif sum(lst)>mon:
           lst.pop()
           n=n+1
​
   op={'product':"",'change':[]}
   for i in products:
    if product_number in i.values():
        op['product']=i['name']
        tot=money-i['price']
        if tot>=0:
          changlst=[]
          chmon(tot,changlst)
        else:
            return 'Not enough money for this product'
   op['change']=changlst
   return op

