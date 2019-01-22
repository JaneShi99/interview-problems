def climb_stairs(n,k):
    """
    construct an array of size n, called dp,
    where dp(i) records the number of ways to reach there
    if i = 1 then return 0
    if i <= k return :
            1 + loop through dp[1]+...+dp[i-1]
    if i > k return:
            loop through dp[k-n]+....+dp[k-1]
            
    """
    dp = [0]* n
    dp[0]=1
    for i in range(1,n):
        if i <= k:
            dp[i] = 1 + sum(dp[j] for j in range(1,i))
        else:
            dp[i] = sum(dp[j] for j in range(1,i))
            
    return dp[-1]

def main():
    print(climb_stairs(10,5))

main()
