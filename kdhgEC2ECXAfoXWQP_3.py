
def transpose_matrix( m ):
    return ' '.join( m[i][j] for j in range(len(m[0])) for i in range(len(m)) )

