class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        result = [0] * len(temperatures)
        waiting_indices = []

        for idx, temp in enumerate(temperatures):
            
            while waiting_indices and temperatures[waiting_indices[-1]] < temp:
                prev_idx = waiting_indices.pop()
                result[prev_idx] = idx - prev_idx
            
            waiting_indices.append(idx)

        return result
