class Solution:
    # Most optimized DP+BS
    def maxEnvelopes(self, arr: List[List[int]]) -> int:    
        def bs(target):
            l=0
            r=len(temp)-1

            while(l<=r):
                mid=(l+r)//2
                if temp[mid]<target:
                    l=mid+1
                else:
                    r=mid-1
            return l

        arr.sort(key=lambda x:(x[0],-x[1]))
        print(arr)
        temp=[]
        for i in range(len(arr)):
            if len(temp)==0 or arr[i][1]>temp[-1]:
                temp.append(arr[i][1])
            else:
                # previous greatest element
                idx=bs(arr[i][1])
                temp[idx]=arr[i][1]
        
        return len(temp)

# Tabulation Code
class Solution1:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
        arr.sort(key = lambda x:x[0])
        print(arr)
        dp=[1 for i in range(len(arr))]
        for i in range(len(arr)-2,-1,-1):
            for j in range(i+1,len(arr)):
                if arr[i][0]<arr[j][0] and arr[i][1]<arr[j][1]:
                    dp[i]=max(dp[i],dp[j]+1)
        return max(dp)

# Memoization Code
class Solution2:
    def maxEnvelopes(self, arr: List[List[int]]) -> int:
       
        def f(idx):
            if idx==len(arr):
                return 0
            
            if dp[idx]!=-1:
                return dp[idx]

            s=0
            for i in range(idx+1,len(arr)):
                if arr[idx][0]<arr[i][0] and arr[idx][1]<arr[i][1]:
                    s=max(s,1+f(i))
            dp[idx]=s
            return dp[idx]

        arr.sort(key = lambda x:x[0])
        print(arr)
        dp=[-1 for i in range(len(arr))]
        
        for i in range(len(arr)):
            f(i)
                
        print(dp)
        return max(dp)+1
        