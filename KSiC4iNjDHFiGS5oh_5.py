
def is_super_d(num):
  print(num);
  super_ds  =  [d for d in range(2,10) if str(d)*d in str(d*(num**d))];
  return "Super-{0} Number".format(super_ds[0]) if len(super_ds) > 0 else "Normal Number";

