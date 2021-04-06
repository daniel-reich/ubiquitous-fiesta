
def does_just_one_pair_add_to_n(known, n):
    all_solutions = {(ulam_num, n-ulam_num) for ulam_num in known if n-ulam_num in known and ulam_num<n/2}
    return len(all_solutions) == 1
​
def ulam(n):
    known, candidate, last = {1,2}, 1, 1
    while len(known)<n:
        if does_just_one_pair_add_to_n(known, candidate):
            known.add(candidate)
            last = candidate
        candidate += 1
    return last if n != 2 else 2

