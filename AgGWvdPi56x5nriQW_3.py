
def longest_slide(pyramid):
    lrow = [pyramid[0][0] + pyramid[1][0], pyramid[0][0] + pyramid[1][1]]
    for prow in pyramid[2:]:
        nrow = [lrow[0] + prow[0]]
        for i in range(1, len(prow) - 1):
            nrow.append(prow[i] + max(lrow[i-1], lrow[i]))
        nrow.append(lrow[1] + prow[-1])
        lrow = nrow[:]
    return max(lrow)

