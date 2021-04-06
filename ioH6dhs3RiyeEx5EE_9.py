
def make_fun_lst(n1, n2):
          return [(lambda x, k=k: x + k) if k%2 == 0 else (lambda x, k=k: x * k) for k in range(n1, n2)]

