class Solution:
    def maxSubArray(self, a: List[int]) -> int:
        max = 0
        max_so_far = 0
        for i in a:
            max+=i
            if max_so_far < max:
                max_so_far = max
            if max < 0:
                max = 0
        return max_so_far