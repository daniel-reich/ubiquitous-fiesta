
def parse(terms):
    coeff, const = 0, 0
    term = terms[0]
    if 'x' in term:
        coeff += 1 if term == 'x' else int(term.replace("*x", ""))
    else:
        const += int(term)
    for i in range(1, len(terms), 2):
        sign = 1 if terms[i] == '+' else -1
        term = terms[i+1]
        if 'x*x' in term:
            continue
        if 'x' in term:
            coeff += sign * (1 if term == 'x' else int(term.replace("*x", "")))
        else:
            const += sign * eval(term)
    return coeff, const
​
def solver(eq):
    terms = eq.replace("-", "- ").split()
    idx_eq = terms.index('=')
    left_coeff, left_const = parse(terms[:idx_eq])
    right_coeff, right_const = parse(terms[idx_eq+1:])
    coeff = left_coeff - right_coeff
    const = right_const - left_const
    if coeff == 0:
        return "Infinite solutions"
    sol = const / coeff
    return round(sol, 1)

