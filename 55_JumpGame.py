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
--------------------------------------------------------------------------
1. Problem Explanation

We are given an array nums where:Each element tells us the maximum jump length we can take from that index.
Starting at index 0, we need to check if we can reach the last index of the array.Output true if possible, otherwise false.

2. Core Logic / Concept

This is a Greedy Problem.
The main idea is to keep track of the farthest index you can reach as you iterate through the array.
If at any point your current index is greater than the farthest reachable index, you’re stuck → return false.
If your farthest reach is beyond or equal to the last index, return true.
Think of it like checking if each platform lets you hop far enough to continue.

3. Solution (Greedy Approach)
Step-by-step:
Initialize maxReach = 0 (farthest we can reach so far).
Iterate through the array:
If i > maxReach, you are stuck → return false.
Update maxReach = max(maxReach, i + nums[i]).
If maxReach >= last index, return true.
Finish loop → return true (because we never got stuck).
----------------------------------------------------------------------------------
