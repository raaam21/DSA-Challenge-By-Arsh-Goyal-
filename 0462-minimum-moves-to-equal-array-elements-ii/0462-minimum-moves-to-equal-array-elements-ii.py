class Solution:
    def minMoves2(self, nums: List[int]) -> int:
        nums.sort()
        if len(nums)%2!=0:
            median=nums[len(nums)//2]
        else:
            median=(nums[len(nums)//2]+nums[(len(nums)//2)-1])//2
        ans=0
        for i in nums:
            ans+=abs(i-median)
        return ans