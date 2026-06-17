class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        if not nums:
            return 0 
        cur_max = 0 
        cur = 0
        nums = sorted(list(set(nums)))
        
        for i in range(len(nums) - 1):
            if nums[i] + 1 == nums[i+1]:
                cur += 1 
                cur_max = max(cur, cur_max)
            else:
                cur = 0 
                continue
        return cur_max + 1