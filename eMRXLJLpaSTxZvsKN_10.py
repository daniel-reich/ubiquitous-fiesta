
def is_ladder_safe(ldr):
    n_rows, n_cols = len(ldr), len(ldr[0])
    if n_cols < 5:
        return False
    no_rung = '#' + ' ' * (n_cols - 2) + '#'
    rung = '#' * n_cols
    if not (ldr[0] == no_rung and ldr[-1] == no_rung and ldr[1] == rung):
        return False
    rung_positions = [((1 if ldr[r] == rung else 0)
                       if ldr[r] in [rung, no_rung] else 2)
                      for r in range(2, n_rows - 1)]
    if 2 in rung_positions or 1 not in rung_positions:
        return False
    gap_len = rung_positions.index(1)
    if not (gap_len < 4
            and rung_positions[: gap_len + 1] * rung_positions.count(1)
            == rung_positions):
        return False
    return True

