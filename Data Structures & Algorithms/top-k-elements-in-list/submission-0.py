from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:

        num_count = Counter(nums)
        frequencies = [0] * k
        elements = [0] * k

        for num, freq in num_count.items():
            if freq > min(frequencies):
                idx = frequencies.index(min(frequencies))
                frequencies[idx] = freq
                elements[idx] = num

        return elements

        