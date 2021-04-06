
def add_bill(money):
   return sum([int(m[1:-1])*1000 if m[0] == "d" and m[-1] == "k" \
   else int(m[1:]) if m[0] == "d" \
   else 0 for m in money.split(",")])

