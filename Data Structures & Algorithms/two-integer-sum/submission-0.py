class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        index_of_num = {}

        for i, num in enumerate(nums):
            diff = target - num

            if diff in index_of_num:
                return [index_of_num[diff], i]
            
            index_of_num[num] = i

        return [0,0]
        