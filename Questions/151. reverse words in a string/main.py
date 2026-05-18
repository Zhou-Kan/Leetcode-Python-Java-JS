# Input: s = "the sky is blue"
# Output: "blue is sky the"
def reverse_words(s: str) -> str:
    lst = s.split()
    lst.reverse()
    return ' '.join(lst)

print(reverse_words("the sky is blue"))