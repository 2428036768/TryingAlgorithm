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
            # 初始化dp二维数组
            dp = np.zeros((N+1, W+1))
            # 对N个物品进行选择
            for i in range(1, N+1):
                # 对i个物品时计算每个W的最优解
                for w in range(1, W+1):
                    # 如果背包装不下了，则不装如第i个物品
                    if w-wt[i-1] < 0:
                        dp[i][w] = dp[i-1][w]
                    # 能装下时，选择价值最大的装法，不装第i个/装第i个
                    else:
                        dp[i][w] = max(dp[i-1][w], dp[i-1][w-wt[i-1]]+val[i-1])
            return dp[N][W]

        # 0/1背包变体，分割等和子集：给定一个只包含正整数的非空数组，是否可以将这个数组分割成两个子集，使得两个子集的元素和相等
        # 转换为使用N个重量不同的物体，寻找一种能将载重为sum/2的背包装满的方法。如果找到即返回
        def canPartition(num):
            Sum = np.sum(num)
            if Sum % 2:
                return False
            # 初始化dp数组
            dp = np.zeros((len(num)+1, int(Sum/2+1))).astype(np.bool_)
            # 当背包负重为0时，就相当于找了将背包装满的方法。因此全部为true
            # dp.fill(False)
            dp[:, 0] = True
            for i in range(1, len(num)+1):
                # 遍历所有的数字
                for w in range(1, int(Sum/2)+1):
                    # 遍历计算每个背包重量
                    if w-num[i-1] < 0:
                        # 装不下，则不装
                        dp[i][w] = dp[i-1][w]
                        # print(dp[i-1][w])
                    else:
                        # 装得下，选择装，或者不装
                        dp[i][w] = dp[i-1][w] or dp[i-1][w-num[i-1]]
            return dp[len(num)][int(Sum/2)]

    class Interview:
        # 编辑距离：给定两个字符串，计算将S1转换成S2能用的最少的操作数（操作包括：删除、替换、插入）
        # 这里将递归（自顶向下）改成了dp数组（自底向上）的操作方法，因此，数组中使用的是i-1和j-1来实现的操作。实际上是从后向前改变字符串
        def minDistance(s1, s2):
            # i\j为两个字符串的长度
            m = len(s1)
            n = len(s2)
            dp = np.zeros((m+1, n+1))
            #base case
            dp[:, 0] = m  # 若s2长度为0，则需要len(s1)个操作：将第一列赋为m
            dp[0, :] = n  # 若s1长度为0，则需要len(s2)个操作：将第一列赋为n
            dp[0][0]=0
            #自底向上求解
            for i in range(1, m+1):
                for j in range(1, n+1):
                    if s1[i-1] == s2[j-1]:
                        dp[i][j]=dp[i-1][j-1]  #不变，继承上一步
                    else:
                        dp[i][j]=min(dp[i-1][j]+1,   #删除s1[i]
                            dp[i][j-1]+1,
                            dp[i-1][j-1]+1
                            )
            return dp[m][n]

if __name__ == "__main__":
    # print(Dynamic_programming.Fibonacci.fib(8))
    # print(Dynamic_programming.CoinChange.CoinChange([1,2,5],10))
    # print(Dynamic_programming.knapsack0_1.knapsack(3,4,[2,1,3],[4,2,3]))
    # print(Dynamic_programming.knapsack0_1.canPartition([2, 2]))
    print(Dynamic_programming.Interview.minDistance('horse','ros'))
