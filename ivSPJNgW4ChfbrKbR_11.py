
def soroban(frame):
    def compute_row(row, ii):
        return (5*(row[0]=='|') + row[3:].index('|'))*10**(7-ii)
    return sum(compute_row(row, ii) for ii, row in enumerate(zip(*frame),1))

