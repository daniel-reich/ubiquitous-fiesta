
def triangle(p, area):
    const, sol, r = round(2*area**2/p, 3), [], range(1, round(p/2+0.1))
    sol = [tuple(sorted((a, b, p-a-b))) for a in r for b in r
           if (p/2-a)*(p/2-b)*(a+b-p/2)==const]
    return sorted([list(i) for i in set(sol)])

