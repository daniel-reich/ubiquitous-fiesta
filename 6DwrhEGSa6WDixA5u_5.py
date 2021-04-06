
is_narcissistic=lambda n:sum(int(x)**len(str(n))for x in str(n))==n

