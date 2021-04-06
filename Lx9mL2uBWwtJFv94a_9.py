
def checker_board(num,option1,option2):
    main=[]
    if option1==option2:
        return 'invalid'
    for i in range(num):
        local=[]
        for j in range(num):
            if i%2:
                if j%2:
                    local.append(option1)
                else:
                    local.append(option2)
            else:
                if j%2:
                    local.append(option2)
                else:
                    local.append(option1)
                
        main.append(local)
    return main

