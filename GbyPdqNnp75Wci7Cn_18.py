
def count_ones(num):
    return sum([ 1 for n in bin(num)[2:] if n == '1'])

