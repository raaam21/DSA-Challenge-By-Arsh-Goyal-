import bisect
class Solution1:
    def numFriendRequests(self, ages: List[int]) -> int:
        cnt=0
        for i in range(len(ages)):
            for j in range(len(ages)):
                if i!=j:
                    if not(ages[i]<=0.5*ages[j]+7 or ages[i] > ages[j] or (ages[i] > 100 and ages[j] < 100)):
                        cnt+=1
        return cnt
class Solution:
    def numFriendRequests(self, nums: List[int]) -> int:
        
        max_lim=0
        nums.sort()
        ans=0
        for i in range(len(nums)):
            l=bisect.bisect_right(nums,(nums[i]*0.5)+7)
            r=bisect.bisect_right(nums,nums[i])
            ans+=max(r-l-1,0)
        return ans



