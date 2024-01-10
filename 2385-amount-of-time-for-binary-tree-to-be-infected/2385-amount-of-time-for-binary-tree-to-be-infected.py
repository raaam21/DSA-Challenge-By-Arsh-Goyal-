# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        def f(root):
            if root is None:
                return

            if root.left:
                graph[root.val].append(root.left.val)
                graph[root.left.val].append(root.val)
                f(root.left)
            if root.right:
                graph[root.val].append(root.right.val)
                graph[root.right.val].append(root.val)
                f(root.right)

            return         

        graph=defaultdict(list)
        f(root)

        print(graph)
        q=[]
        time=0
        q.append(start)
        vis=set()
        while(len(q)>0):
            sz=len(q)
            for _ in range(sz):
                node=q.pop(0)
                vis.add(node)
                for nbr in graph[node]:
                    if nbr not in vis:
                        q.append(nbr)

            time+=1
        
        return time-1
