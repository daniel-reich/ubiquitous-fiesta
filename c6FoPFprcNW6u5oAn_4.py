
def farey(n):
    numbers = []
    results = []
    org_results = []
    sol = []
    real_sol = []
    for x in range(n+1):
        numbers.append(x)
​
​
​
    for x in range(len(numbers)):
        for y in numbers:
            if y != 0:
                z = numbers[x] / y
                if z not in results and z < 1:
                    results.append(z)
                    sol.append(str(numbers[x])+"/"+str(y))
​
    for x in results:
        org_results.append(x)
    results.sort()
​
    for x in results:
​
        real_sol.append(sol[org_results.index(x)])
    real_sol.append("1/1")
    print(real_sol)
    return real_sol

