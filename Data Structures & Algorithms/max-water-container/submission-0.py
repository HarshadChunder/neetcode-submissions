class Solution:
    def maxArea(self, heights: List[int]) -> int:

        left, right = 0, len(heights) - 1
        best = 0

        while left < right:
            area = min(heights[left], heights[right]) * abs(right - left)

            if area > best:
                best = area
            elif heights[left] > heights[right]:
                right -= 1
            else:
                left += 1
        
        return best


        