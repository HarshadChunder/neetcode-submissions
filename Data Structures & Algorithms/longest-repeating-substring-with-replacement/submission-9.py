from collections import defaultdict

class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = 0
        best_length = 0
        repeat_count = 0
        letter_counts = defaultdict(int)

        for right in range(len(s)):
            letter_counts[s[right]] += 1
            repeat_count = sum(value for value in letter_counts.values()) - max(letter_counts.values())

            while repeat_count > k:           
                letter_counts[s[left]] -= 1
                repeat_count = sum(value for value in letter_counts.values()) - max(letter_counts.values())

                left += 1

            best_length = max(best_length, right - left + 1)

        return best_length
        