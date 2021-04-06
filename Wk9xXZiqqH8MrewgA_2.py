
digits = {"111101101101111": '0', "010110010010111": '1',
          "111001111100111": '2', "111001111001111": '3',
          "101101111001001": '4', "111100111001111": '5',
          "100100111101111": '6', "111001001001001": '7',
          "111101111101111": '8', "111101111001001": '9'}
rev_digits = {v: k for k, v in digits.items()}
​
def get_bits(rows, k):
    for j in range(5):
        rows[j] += rev_digits[k][3*j:3*j+3]
    return rows
​
def append_blank_col(rows):
    for j in range(5):
        rows[j] += "0"
    return rows
​
def to_bit_string(time):
    rows = ["", "", "", "", ""]
    rows = get_bits(rows, time[0])
    rows = append_blank_col(rows)
    rows = get_bits(rows, time[1])
    rows = append_blank_col(rows)
    for i in [0, 2, 4]:
        rows[i] += "0"
    for i in [1, 3]:
        rows[i] += "1"
    rows = append_blank_col(rows)
    rows = get_bits(rows, time[3])
    rows = append_blank_col(rows)
    rows = get_bits(rows, time[4])
    return ''.join(rows)

