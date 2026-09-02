class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        num_list = set(nums)

        result = 0

        for i in num_list:
            if i-1 not in num_list:
                count = 1
                up = i+1
                while(up in num_list):
                    count += 1
                    up += 1
                    
                if count > result:
                    result = count

        return result