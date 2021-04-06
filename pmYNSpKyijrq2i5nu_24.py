
def darts_solver(sections, darts, target):
    result = []
​
    def find_solution(solution):
        if len(solution) < darts:
            for i in sections:
                part_solution = solution[:]
                part_solution.append(i)
                find_solution(part_solution)
        else:
            if sum(solution) == target:
                for i in result:
                    if set(solution) == set(i):
                        break
                else:
                    result.append(solution)
​
    find_solution([])
    return ['-'.join(map(str, x)) for x in result]

