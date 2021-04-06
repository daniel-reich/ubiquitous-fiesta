
def loves_me(n):
    return 'Loves me, Loves me not, ' * ((n-1) // 2) + \
          ('Loves me, LOVES ME NOT', 'LOVES ME')[n % 2]

