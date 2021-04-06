
def longest_run(lst):
    run_lens = []
    for i in range(len(lst)):
        run = 1
        num = lst[i]
        check = None
        for a in lst[i+1:]:
            if not check:
                check = 'up' if num - a < 0 else 'down'
            run_dir = 'up' if num - a < 0 else 'down'
            if abs(num - a) == 1 and run_dir == check:
                run +=1
                num = a
        run_lens.append(run)
    return max(run_lens)

