class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left, max_len = 0, 0
        substring = ""

        for right in range(len(s)):
            if s[right] not in substring:
                substring += s[right]
                max_len = max(max_len, len(substring))
            else:
                left = substring.index(s[right])
                substring = substring[left + 1:] + s[right]

        return max_len

"""
Heres a better way:

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        window_chars = set()
        left = 0
        max_len = 0

        for right in range(len(s)):
            while s[right] in window_chars:
                window_chars.remove(s[left])
                left += 1
            window_chars.add(s[right])
            max_len = max(max_len, right - left + 1)

        return max_len
"""