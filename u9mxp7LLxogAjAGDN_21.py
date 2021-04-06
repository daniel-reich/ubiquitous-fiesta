
def factor_sort(lst):
    def factors_and_num(num):
        def factors(num, factor = 1):
            if 2*factor > num:
                return 1
            greater_factors = factors(num, factor + 1)
            if num%factor == 0:
                return 1 + greater_factors
            return greater_factors
        return (factors(num), num)
    return list(sorted(lst, key = factors_and_num, reverse = True))

