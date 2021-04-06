
def tf_lst(A):
    ref = A[4]
    return A[0] == 10 + ref / 10. and \
           A[1] == 2 * ref and \
           A[2] == int(pow(ref, .5)) and \
           A[3] == 321 * ref and \
           A[5] == ref + A[2] and \
           A[6] == ref**2 and \
           A[7] == round(ref * 1.2, 1)

