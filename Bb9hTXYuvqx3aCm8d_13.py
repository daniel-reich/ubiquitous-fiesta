
def alpha_clash(str_A, ind_A, str_Z, ind_Z):
    player_a_total = 0
    player_z_total = 0
    
    list_of_a = list(str_A)
    list_of_z = list(str_Z)
    
    ind_A.sort(reverse = True)
    ind_Z.sort(reverse = True)
    
    for i in ind_A:
        del list_of_z[i]
    
    for j in ind_Z:
        del list_of_a[j]
    
    for i in range(len(list_of_a)):
        list_of_a[i] = ord(list_of_a[i])
        list_of_z[i] = ord(list_of_z[i])
        
    for i in range(len(list_of_z)):
        if list_of_a[i] > list_of_z[i]:
            player_a_total += list_of_a[i]-list_of_z[i]
        elif list_of_z[i] > list_of_a[i]:
            player_z_total += list_of_z[i]-list_of_a[i]
    
    return {'A': player_a_total, 'Z': player_z_total}

