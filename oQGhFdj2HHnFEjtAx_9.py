
def slicer(s, slc):
    lst_idx = [s.index(c) for c in slc]
    if len(lst_idx) == 1 and len(s) > 1:
        return '[{}]'.format(lst_idx[0])
    else:
        step = lst_idx[1] - lst_idx[0]
        if step > 0:
            begin = '' if lst_idx[0] == 0 else lst_idx[0]
            end = '' if lst_idx[-1] + step >= len(s) else lst_idx[-1]
            if step == 1:
                return '[{}:{}]'.format(str(begin),
                                        str(end + 1) if end else end)
            else:
                return '[{}:{}:{}]'.format(str(begin),
                                           str(end + 1) if end else end,
                                           str(step))
        elif step < 0:
            begin = '' if lst_idx[0] == len(s) - 1 else lst_idx[0]
            end = '' if lst_idx[-1] + step < 0 else lst_idx[-1]
            return '[{}:{}:{}]'.format(str(begin),
                                       str(end - 1) if end else end,
                                       str(step))

