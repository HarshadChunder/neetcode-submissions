from collections import Counter

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if len(s1) > len(s2):
            return False
        
        left = 0
        substring = s2[:len(s1)]
        Counter1 = Counter(s1)
        Counter2 = Counter(substring)

        for right in range(len(s1), len(s2)):
            if Counter1 == Counter2:
                return True

            Counter2[s2[right]] += 1
            Counter2[s2[left]] -= 1

            left += 1

        if Counter1 == Counter2:
                return True

        return False
            





