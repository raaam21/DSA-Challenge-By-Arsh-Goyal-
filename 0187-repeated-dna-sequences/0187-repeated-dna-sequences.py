class Solution1:
    # Brute Force
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        ans=set()
        for i in range(len(s)):
            if s[i:i+10] in s[i+1:]:
                ans.add(s[i:i+10])
        return ans

class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        hm=defaultdict(int)
        for i in range(len(s)):
            hm[s[i:i+10]]+=1
        ans=[]
        for k,v in hm.items():
            if v>=2:
                ans.append(k)
        return ans