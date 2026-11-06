class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        countLeft, countRight = 1, 1
        left, right = [countLeft], [countRight]

        for i in range(1, len(nums)):
            countLeft *= nums[i - 1]
            left.append(countLeft)

        for i in range(len(nums) - 2, -1, -1):
            countRight *= nums[i + 1]
            right.append(countRight)

        right = right[::-1]

        return [left[i] * right[i] for i in range(len(nums))]

            
        