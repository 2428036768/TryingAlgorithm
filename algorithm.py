"""
算法框架学习
"""
import numpy as np


"""
动态规划
"""


class Dynamic_programming:
    # 利用dp数组进行优化

    # 求第n个斐波那契数
    class Fibonacci:
        def fib(n):
            if n == 1 or n == 2:
                return 1
            f = np.zeros(n+1)
            f[1] = 1
            f[2] = 1
            for i in range(3, n+1):
                f[i] = f[i-1]+f[i-2]
            return f[n]

    # 凑零钱问题:给你k种面值的硬币，面值分别为c1, c2 ... ck，每种硬币的数量无限，再给一个总金额amount，问你最少需要几枚硬币凑出这个金额，如果不可能凑出，算法返回 -1 。
    class CoinChange:
        # coins：零钱面额   amount：总金额
        def CoinChange(coins, amount):
            if amount == 0:
                return 0
            dp = [amount+1]*(amount+1)
            dp[0] = 0
            for i in range(1, amount+1):
                for coin in coins:
                    if i-coin < 0:
                        continue
                    dp[i] = min(dp[i], dp[i-coin]+1)
            return dp[amount]

    # 0/1背包问题：给你一个可装载重量为W的背包和N个物品，每个物品有重量和价值两个属性。其中第i个物品的重量为wt[i]，价值为val[i]，现在让你用这个背包装物品，最多能装的价值是多少？
    class knapsack0_1:
        # N=3
        # W=5
        # wt = [2, 1, 3]
        # val = [4, 2, 3]
        
        def knapsack(N, W, wt, val):
            #初始化dp二维数组
            dp = np.zeros((N+1, W+1))   
            #对N个物品进行选择
            for i in range(1, N+1):     
                #对i个物品时计算每个W的最优解
                for w in range(1, W+1):   
                    #如果背包装不下了，则不装如第i个物品
                    if w-wt[i-1]<0:          
                        dp[i][w]=dp[i-1][w]
                    #能装下时，选择价值最大的装法，不装第i个/装第i个
                    else:                     
                        dp[i][w]=max(dp[i-1][w], dp[i-1][w-wt[i-1]]+val[i-1])
            return dp[N][W]

if __name__ == "__main__":
    # print(Dynamic_programming.Fibonacci.fib(8))
    # print(Dynamic_programming.CoinChange.CoinChange([1,2,5],10))
    print(Dynamic_programming.knapsack0_1.knapsack(3,4,[2,1,3],[4,2,3]))
    