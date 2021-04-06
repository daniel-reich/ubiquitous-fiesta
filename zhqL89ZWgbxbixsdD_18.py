
is_exact = lambda val,acc=1,num=1: [val, num] if val == acc else \
           'Not exact!' if acc > val else is_exact(val,acc*(num+1),num+1)

