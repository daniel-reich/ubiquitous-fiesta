
def tune(lst):
    tunes = (329.63, 246.94, 196.00, 146.83, 110.00, 82.41)
    res = []
    for frequency in lst:
        if frequency == 0:
            res.append(' - ')
        else:
            diff = [abs(frequency - t) for t in tunes]
            min_diff_idx = diff.index(min(diff))
            rel_diff = round(diff[min_diff_idx] / tunes[min_diff_idx], 2)
            if rel_diff < 0.01:
                res.append('OK')
            elif rel_diff < 0.03:
                if frequency < tunes[min_diff_idx]:
                    res.append('>+')
                else:
                    res.append('+<')
            else:
                if frequency < tunes[min_diff_idx]:
                    res.append('>>+')
                else:
                    res.append('+<<')
    return res

