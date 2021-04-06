
def max_possible(n1, n2):
    n2_img = sorted(str(n2), reverse = True)
    n1_img = list(str(n1))
    for j, c in enumerate(n2_img):
        for i, h in enumerate(n1_img):
            if int(c) > int(h):
                n1_img[i] = n2_img[j]
                break
    return int(''.join(n1_img))

