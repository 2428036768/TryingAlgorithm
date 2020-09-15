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


if __name__ == "__main__":
    # print(Dynamic_programming.Fibonacci.fib(8))
    # print(Dynamic_programming.CoinChange.CoinChange([1,2,5],10))
