# Example 1:

# Input: low = 3, high = 3, zero = 1, one = 1
# Output: 8
# Explanation: 
# One possible valid good string is "011". 
# It can be constructed as follows: "" -> "0" -> "01" -> "011". 
# All binary strings from "000" to "111" are good strings in this example.
# Example 2:

# Input: low = 2, high = 3, zero = 1, one = 2
# Output: 5
# Explanation: The good strings are "00", "11", "000", "110", and "011".
def count_good_strings(low: int, high: int, zero: int, one: int) -> int:
    MOD = 100_000_007
    dp = [0] * (high + 1)
    
    dp[0] = 1
    for i in range(low, high + 1):
        dp[i] = dp[i - zero] + dp[i - one]
        