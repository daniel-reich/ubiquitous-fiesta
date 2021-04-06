
endings = ["are", "ere", "ire"]
​
def inflect(verb,person,number):
    base, ending = verb[:-3], verb[-3:]
    ans = pronomi[person][number] + " " + base
    ans += verbi_spec[person][number][endings.index(ending)]
    ans += verbi_com[person][number]
    return ans

