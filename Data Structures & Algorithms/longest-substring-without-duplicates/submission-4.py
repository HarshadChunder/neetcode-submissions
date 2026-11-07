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