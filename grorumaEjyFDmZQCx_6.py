
def is_wristband(lst):
    n_rows, n_cols = len(lst), len(lst[0])
    max_len = max(n_rows, n_cols)
    h_pattern, v_pattern, dl_pattern, dr_pattern = True, True, True, True
    for i in range(n_rows):
        if len(set(lst[i])) != 1:
            h_pattern = False
            break
    for tpl in zip(*lst):
        if len(set(tpl)) != 1:
            v_pattern = False
            break
    i = 0
    for j in range(n_cols):
        pos_row, pos_col = i, j
        line = []
        for k in range(max_len):
            if pos_row + k < n_rows and pos_col + k < n_cols:
                line.append(lst[pos_row + k][pos_col + k])
            else:
                break
        if len(set(line)) != 1:
            dl_pattern = False
            break
    j = 0
    for i in range(n_rows):
        pos_row, pos_col = i, j
        line = []
        for k in range(max_len):
            if pos_row + k < n_rows and pos_col + k < n_cols:
                line.append(lst[pos_row + k][pos_col + k])
            else:
                break
        if len(set(line)) != 1:
            dl_pattern = False
            break
    i = 0
    for j in range(n_cols):
        pos_row, pos_col = i, j
        line = []
        for k in range(max_len):
            if pos_row + k < n_rows and pos_col - k > -1:
                line.append(lst[pos_row + k][pos_col - k])
            else:
                break
        if len(set(line)) != 1:
            dr_pattern = False
            break
    j = n_cols - 1
    for i in range(n_rows):
        pos_row, pos_col = i, j
        line = []
        for k in range(max_len):
            if pos_row + k < n_rows and pos_col - k > -1:
                line.append(lst[pos_row + k][pos_col - k])
            else:
                break
        if len(set(line)) != 1:
            dr_pattern = False
            break
    return h_pattern or v_pattern or dl_pattern or dr_pattern

