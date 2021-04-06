
factorial = lambda n: eval('*'.join([str(i) for i in reversed(range(1, n+1))]))
fact_of_fact = lambda n: eval('*'.join([str(factorial(i)) for i in reversed(range(1, n+1))]))

