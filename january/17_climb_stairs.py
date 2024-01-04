def climbStairs(n: int) -> int:
    # Solution 1
    # ways = 1
    #
    # for i in range(1, (n // 2) + 1):
    #     product = 1
    #
    #     for j in range(i, 2 * i):
    #         product *= (n - j) / (j - i + 1)
    #
    #     ways += product
    #
    # return int(ways)

    # Solution 2
    def solve(n, dp):
        if n < 0:
            return 0
        if n == 0:
            return 1

        if dp[n] != -1:
            return dp[n]

        dp[n] = solve(n - 1, dp) + solve(n - 2, dp)

        return dp[n]

    dp = [-1] * (n + 1)
    return solve(n, dp)


print(climbStairs(n=3))
