class Solution:
    def criticalConnections(self, n: int, connections: List[List[int]]) -> List[List[int]]:
        import collections
        
        G = collections.defaultdict(list)
        for edge in connections:
            G[edge[0]].append(edge[1])
            G[edge[1]].append(edge[0])
        self.order = 0
        llink=[]
        ids=[]
        
        for i in range(n):
            llink.append(-1)
            ids.append(-1)

            
        for i in range(n):
            if ids[i] == -1:
                self.DFS(i,None,G,llink,ids)
        
        res=[]
        for edge in connections:
            if llink[edge[1]]>ids[edge[0]] or llink[edge[0]]>ids[edge[1]]:
                res.append([edge[0],edge[1]])
        print(llink)
        return res
    
    def DFS(self, i,parent,G,llink,ids):
    
        ids[i]=self.order
        llink[i]=self.order

        self.order=self.order+1
        for adjacent in G[i]:
            #Here's the main difference from Tarjan's algorithm for directed graph. Unlike Tarjan that uses a stack,
            #here we simply test if we are tracing back to its direct parent.
            if ids[adjacent] == -1:
                self.DFS(adjacent,i,G,llink,ids)
            if parent != None:
                if parent != adjacent:
                    llink[i]=min(llink[i],llink[adjacent])
            else:
                llink[i]=min(llink[i],llink[adjacent])



            