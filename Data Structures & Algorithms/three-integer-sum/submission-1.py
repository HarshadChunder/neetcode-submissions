class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums_sorted = sorted(nums)
        triplets = []

        for current in range (len(nums_sorted) - 2):
            anchor = nums_sorted[current]

            if anchor > 0:
                break
            
            if current > 0 and nums_sorted[current] == nums_sorted[current - 1]:
                continue

            left = current + 1
            right = len(nums_sorted) - 1

            while left < right:
                total = nums_sorted[left] + nums_sorted[right] + anchor

                if total < 0:
                    left += 1
                elif total > 0:
                    right -=1
                else:
                    triplets.append([nums_sorted[left], nums_sorted[current], nums_sorted[right]])
                    left += 1
                    right -=1

                    while left < right and nums_sorted[left] == nums_sorted[left - 1]:
                        left += 1

        return triplets





        