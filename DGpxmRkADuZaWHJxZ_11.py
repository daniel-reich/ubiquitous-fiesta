
def maurice_wins(m_snails, s_snails):
    return sum(m_snails[1:][n] > s_snails[n] for n in range(2)) == 2

