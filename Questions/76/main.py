from collections import Counter

def min_window(s: str, t: str) -> str:
    m, n = len(s), len(t)
    ans = ''
    if m < n:
        return ans
    
    count = Counter(t)
    letters = len(count)

    max_len = m
    

    left = right = 0
    while right < m:
        c = s[right]
        if c in count:
            count[c] -= 1
        
        if c in count and count[c] == 0: # 
            letters -= 1
        
        while letters == 0 and left <= right:
            if right - left + 1 <= max_len:
                max_len = right - left + 1
                ans = s[left:right + 1]


            if s[left] in count:
                count[s[left]] += 1
                if count[s[left]] == 1:
                    letters += 1
            
            left += 1
        right += 1
    
    return ans

print(min_window("ADOBECODEBANC", "ABC"))
print(min_window('a', 'a'))

# First, I will create a frequency map to count the occurrences of each character in string t.
# Second, I'll expand the right pointer to slide the window across string s. I will keep expanding until the current window contains all the required character 
# from t
# Finally, once a valid window is found, I will contract the window by moving the left pointer forward. This allows me to shrink the window, look for the minimum size 
# size 
        
        

