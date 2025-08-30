class Solution:
    def canJump(self, nums: list[int]) -> bool:
        maxReach = 0
        n = len(nums)
        
        for i in range(n):
            if i > maxReach:  # Stuck, cannot move further
                return False
            maxReach = max(maxReach, i + nums[i])
            if maxReach >= n - 1:  # Can reach the end
                return True
        
        return True
