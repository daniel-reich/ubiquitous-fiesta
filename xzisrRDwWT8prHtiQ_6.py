
def difference_two(lst):
    return sorted(sorted([v, lst[j]]) for i, v in enumerate(lst[:-1])
                  for j in range(i + 1, len(lst)) if abs(v - lst[j]) == 2)

