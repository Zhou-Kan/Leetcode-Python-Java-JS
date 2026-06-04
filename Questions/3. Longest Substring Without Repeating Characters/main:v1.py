from collections import defaultdict
def length_of_longest_substring(s: str) -> int:
    ans = 0
    n = len(s)
    left = right = 0
    count = defaultdict(int)

    while right < n:
        c = s[right]
        count[c] += 1
        while count[c] > 1:
            count[s[left]] -= 1
            left += 1
        
        ans = max(ans, right - left + 1)
        right += 1
    
    return ans

print(length_of_longest_substring('abcabcbb'))
print(length_of_longest_substring('bbbbb'))
print(length_of_longest_substring('pwwkew'))
        
