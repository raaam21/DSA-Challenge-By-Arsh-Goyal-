class Solution1:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:
        # Tried simple dfs but it is a weighted graph so we can't simply apply dfs we have to go with shortest path algo.
        # It can be Dijkstra or Floyd Warshall. Becasuse it does not contain negative weights
        
        def dfs(node,weight):
            if node in vis or weight>distanceThreshold:
                return 0

            vis.add(node)
            ans=1
            for nbr,w in graph[node]:
                if nbr not in vis and weight+w<=distanceThreshold:
                    ans+=dfs(nbr,weight+w)
            return ans
        
        graph=defaultdict(list)
        for a,b,c in edges:
            graph[a].append([b,c])
            graph[b].append([a,c])
        ans=[]
        for i in range(n):
            vis=set()
            ans.append([i,dfs(i,0)-1])
        ans.sort(key=lambda x:(x[1],-x[0]))
        print(graph)
        print(ans)
        return ans[0][0]

class Solution:
    def findTheCity(self, n: int, edges: List[List[int]], distanceThreshold: int) -> int:


        def bfs(node):
            q=[]
            heappush(q,[0,node])
            vis=set()
            while(len(q)>0):
                sz=len(q)
                for _ in range(sz):
                    wt,x=heappop(q)
                    vis.add(x)
                    for nbr,w in graph[x]:
                        if nbr not in vis and w+wt<=distanceThreshold:
                            heappush(q,[w+wt,nbr])
            return len(vis)

        graph=defaultdict(list)
        for a,b,c in edges:
            graph[a].append([b,c])
            graph[b].append([a,c])
        ans=[]
        for i in range(n):
            ans.append([i,bfs(i)])
        ans.sort(key=lambda x:(x[1],-x[0]))
        return ans[0][0]