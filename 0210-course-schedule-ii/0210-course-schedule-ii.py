class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        adj={i:[] for i in range(numCourses)}
        indegree={i:0 for i in range(numCourses)}
        ans=[]

        for dest,src in prerequisites:
            adj[src].append(dest)
            indegree[dest]+=1
        q=[]
        for node,ind in indegree.items():
            if ind==0:
                q.append(node)
        
        while(q):
            cur=q.pop(0)
            ans.append(cur)

            for neigh in adj[cur]:
                indegree[neigh]-=1
                if indegree[neigh]==0:
                    q.append(neigh)

        if len(ans)==numCourses:
            return ans
        else:
            return []