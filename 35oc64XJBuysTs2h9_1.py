
def mdn(lst):
    mid_pos = len(lst) // 2
    if len(lst) % 2:
        return lst[mid_pos]
    return (lst[mid_pos] + lst[mid_pos - 1]) / 2
​
​
def get_quartiles(lst, method):
    lst.sort()
    q0, q4, q2, q1, q3 = lst[0], lst[-1], mdn(lst), 0, 0
    q2 = int(q2) if isinstance(q2, float) and q2.is_integer() else q2
    mid_position = len(lst) // 2
    if method == 'T':
        if len(lst) % 2:
            q1 = mdn(lst[:mid_position + 1])
            q3 = mdn(lst[mid_position:])
        else:
            q1 = mdn(lst[:mid_position])
            q3 = mdn(lst[mid_position:])
    elif method == 'MM':
        if len(lst) % 2:
            q1 = mdn(lst[:mid_position])
            q3 = mdn(lst[mid_position + 1:])
        else:
            q1 = mdn(lst[:mid_position])
            q3 = mdn(lst[mid_position:])
    elif method == 'MS':
        n_q1, n_q3 = (len(lst) + 1) / 4, (len(lst) + 1) * 3 / 4
        if n_q1 - int(n_q1) >= 0.5:
            n_q1 = int(n_q1) + 1
        else:
            n_q1 = int(n_q1)
        if n_q3 - int(n_q3) <= 0.5:
            n_q3 = int(n_q3)
        else:
            n_q3 = int(n_q3) + 1
        q1, q3 = lst[n_q1 - 1], lst[n_q3 - 1]
    return [q0, q1, q2, q3, q4]

