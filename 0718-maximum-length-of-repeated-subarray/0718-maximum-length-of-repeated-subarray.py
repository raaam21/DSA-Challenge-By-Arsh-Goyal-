# Brute Force
class Solution1:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        hm=defaultdict(int)
        for i in range(len(nums1)):
            s=''
            for j in range(i,len(nums1)):
                s+=str(nums1[j])+','
                hm[s]+=1
        ans=0
        for i in range(len(nums2)):
            s=''
            for j in range(i,len(nums2)):
                s+=str(nums2[j])+','
                if s in hm:
                    ans=max(ans,j-i+1)
        return ans

# DP
class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        dp=[[0 for i in range(len(nums2)+1)]for j in range(len(nums1)+1)]
        for i in range(len(nums1)-1,-1,-1):
            for j in range(len(nums2)-1,-1,-1):
                if nums1[i]==nums2[j]:
                    dp[i][j]=dp[i+1][j+1]+1
        
        ans=0
        for i in range(len(dp)):
            for j in range(len(dp[0])):
                ans=max(ans,dp[i][j])
        return ans