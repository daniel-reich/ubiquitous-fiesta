
def maurice_wins(m_snails, s_snails):
    a=0
    if(m_snails[1]>s_snails[0]):
        a=a+1
    if(m_snails[2]>s_snails[1]):
        a=a+1
    if a==2:
        return True
    else:
        return False

