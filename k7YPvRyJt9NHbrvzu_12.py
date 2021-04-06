
def football(score):
    if score == 0:
        return 1
    return sum(2 * n2 + 3 * n3 + 6 * n6 + 7 * n7 + 8 * n8 == score
               for n2 in range(score // 2 + 1)
               for n3 in range((score - 2 * n2) // 3 + 1)
               for n6 in range((score - 2 * n2 - 3 * n3) // 6 + 1)
               for n7 in range((score - 2 * n2 - 3 * n3 - 6 * n6) // 7 + 1)
               for n8 in range((score - 2 * n2 - 3 * n3 - 6 * n6 - 7 * n7)
                               // 8 + 1))

