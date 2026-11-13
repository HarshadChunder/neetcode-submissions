import math

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        sum_piles = sum(piles)
        min_rate = math.ceil(sum_piles / h)
        max_rate = max(piles)

        def check_piles(eating_rate):
            return sum([math.ceil(banana_pile / eating_rate) for banana_pile in piles]) <= h

        left, right, best = min_rate, max_rate, max_rate

        while left < right:
            mid = (left + right) // 2

            if check_piles(mid) == True:
                right = mid
                best = mid
            else:
                left = mid + 1

        return best