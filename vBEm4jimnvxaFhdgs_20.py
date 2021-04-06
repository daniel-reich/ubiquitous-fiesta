
def years_in_one_house(age, moves):
    if moves == 0:
        return(age)
    else:
        return (round(age/(moves+1)))

