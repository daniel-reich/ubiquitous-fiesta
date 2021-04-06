
def matrix_mult(m1, m2):
    """Number of rows in m1 must equal columns in m2"""
    m3 = []
    for m1_row in m1:
        m3_row = []
        for i in range(len(m1_row)):
            m3_val = 0
            for j in range(len(m1_row)):
                m3_val += m1_row[j] * m2[j][i]
            m3_row.append(m3_val)
        m3.append(m3_row)
    return m3

