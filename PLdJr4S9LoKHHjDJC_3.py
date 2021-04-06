
def identify(*cube):
    H, W = len(cube), len(cube[0])
    full_row = ["O"] * W
    if all([row == full_row for row in cube]):
        return "Full" if H == W else "Non-Full"
    max_len = max([len(row) for row in cube])
    return "Missing " + str(max_len * H - sum([len(row) for row in cube]))

