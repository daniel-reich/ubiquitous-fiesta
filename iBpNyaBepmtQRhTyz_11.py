
def c_cipher(msg, key):
    '''
    Returns encrypted / decrypted msg using key for columnar cipher
    '''
    from math import ceil
    
    m_size, k_size = len(msg), len(key)
    s_key = sorted(key)
    encrypting = not(msg.isalnum() and msg.islower()) or \
                 m_size != m_size // k_size * k_size
​
    if encrypting:
        k_map = {key.index(l):s_key.index(l) for l in key}
        msg = ''.join(c.lower() for c in msg if c.isalnum())
        msg += 'x' * (ceil(len(msg) / k_size) * k_size - len(msg))
        m_size = len(msg)
        rows = [sorted([(msg[j],j) for j in range(i, i+k_size)],
                           key=lambda x: k_map[x[1]%k_size])
                    for i in range(0,m_size,k_size)]
​
        rows = [''.join([row[i][0] for i in range(len(row))]) for row in rows]
​
        return ''.join(''.join(i for i in col) for col in zip(*rows))
        
    else:  # decrypting
        k_map = {key.index(l):s_key.index(l) * (m_size // k_size) for l in key}
        rows = [''.join([msg[(k_map[i]+j)%m_size] for i in sorted(k_map.keys())])
                for j in range(m_size // k_size)]
        
        return ''.join(''.join(l for l in row) for row in rows)

