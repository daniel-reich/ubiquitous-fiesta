
def build_staircase_up(n, level, sc):
    level += 1
    sc += '_' * (n - level) + '#' * level + '\n'
    return sc[:-1] if level == n else build_staircase_up(n, level, sc)
​
def build_staircase_down(n, level, sc):
    level -= 1
    sc += '_' * (n - level) + '#' * level + '\n'
    return sc[:-1] if level == 1 else build_staircase_down(n, level, sc)
    
def staircase(n):
    return build_staircase_up(n, 0, "") if n > 0 else build_staircase_down(abs(n), abs(n) + 1, "")

