from bisect import bisect_left

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        idx = []
        for i in nums:
            position = bisect_left(idx, i)
            if position == len(idx):
                idx.append(i)
            else:
                idx[position] = i

        
        return len(idx)
                    