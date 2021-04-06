
def golomb(n):  
    x=[]
    dp = [0] * (n + 1)
    dp[1] = 1
    x.append(dp[1]) 
    for i in range(2, n + 1):  
      
        dp[i] = 1 + dp[i - dp[dp[i - 1]]]  
        x.append(dp[i])  
    return x

