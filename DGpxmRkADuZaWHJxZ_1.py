
def maurice_wins(m_snails, s_snails):
    ms, mm, mf = m_snails
    ss, sm, sf = s_snails
    
    return ms < sf and mm > ss and mf > sm

