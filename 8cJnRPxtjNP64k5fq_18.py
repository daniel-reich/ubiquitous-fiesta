
def dance(lst, parameter):
    if parameter=='women':
        w_name=[i[0] for i in lst][::-1]
        m_name=[i[1] for i in lst]
        z=[[w_name[i],m_name[i]] for i in range(len(w_name))]
        return z
    else:
        w_name=[i[0] for i in lst]
        m_name=[i[1] for i in lst][::-1]
        z=[[w_name[i],m_name[i]] for i in range(len(w_name))]
        return z

