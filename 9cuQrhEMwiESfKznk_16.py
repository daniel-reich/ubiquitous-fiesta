
def eng2nums(s):
    nums = {'zero': 0,'one': 1,'two': 2,'three': 3,'four': 4,'five': 5,'six': 6,'seven': 7,'eight':8 ,'nine': 9, 'ten': 10,
    'eleven': 11,'twelve': 12,'thirteen': 13,'fourteen': 14,'fifteen': 15,'sixteen': 16,'seventeen': 17,'eighteen': 18 ,'nineteen': 19,
    'twenty': 20,'thirty': 30,'fourty': 40,'fifty': 50,'sixty': 60,'seventy': 70,'ninety': 90,'hundred':100}
    ans = [nums[i] for i in s.split()]
    total = 0
    for i in range(len(ans)-1):
        if ans[i] < ans[i+1]:
            ans[i+1] *= ans[i]
        else:
            total += ans[i]    
    return total + ans[-1]

