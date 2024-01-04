class Solution:
    def numberOfWays(self, startPos: int, endPos: int, k: int) -> int:
        @cache
        def f(idx,k):
            if idx==endPos and k==0:
                return 1
            if k<0:
                return 0
            
            return ((f(idx+1,k-1)+f(idx-1,k-1))%(10**9+7))
        return f(startPos,k)