
def pop(state):
    result_zero = int(state.count(0))
    return [a for a in range(int(result_zero / 2))] + [sorted(state)[-1]]+ [a for a in range(int(result_zero / 2))][::-1]

