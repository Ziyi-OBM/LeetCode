class Solution:
    def kClosest(self, points: List[List[int]], K: int) -> List[List[int]]:
        
        
        ##Naive solution (sort)
        dist=[]
        for i in range (len(points)):
            dist.append(points[i][0]**2+points[i][1]**2)            
        dist.sort()
        
        Kth=dist[K-1]
        topK=[]
        
        for pt in points:
            if (pt[0]**2+pt[1]**2)<=Kth:
                topK.append(pt)
        
        return topK
    

        ##Naive solution (sort) with better syntax
        points.sort(key=lambda pt : pt[0]**2+pt[1]**2)
        return points[0:K]


        ##Using Heap (and tuple)

        import heapq

        topK=[]
        heapq.heapify(topK)

        for index, pt in enumerate(points): #use enumerate to get the index 
            dist = -(pt[0]**2+pt[1]**2)            
            if index < K:
                #Push in the first K points
                #In the item argument, use a tuple to save the index at the same time
                heapq.heappush(topK,(dist,index))
            else:
                #When a points is closer than current Kth point, pop and push the new point
                if dist>topK[0][0]:
                    heapq.heapreplace(topK,(dist,index))

        res=[]    
        for i in range(K):
            res.append(points[topK[i][1]])

        return res

                
        ##Using quick selection (partition)
        dist=[]
        for index , pt in enumerate(points):
            dist.append((pt[0]**2+pt[1]**2,index))            
        

        low = 0
        high = len(dist)-1
        pivot=self.partition(dist, low, high)
        
        while pivot is not K-1:
            if pivot < K-1:
                low = pivot+1
                pivot=self.partition(dist, low, high)
            if pivot > K-1:
                high = pivot-1
                pivot=self.partition(dist, low, high)  
                
        res=[]
        
        for i in range(K):
            res.append(points[dist[i][1]])
        
        return res

    ##Partition algorithm from quick sort        
    def partition(self, A, lo, hi):
        pivot = A[hi][0]
        
        frontier = lo  #Pointer that propagate and make swaps
        final = lo #Final position that the pivot should be
        
        while frontier < hi:
            if A[frontier][0] < pivot:
                A[final],A[frontier]=A[frontier],A[final]
                final = final + 1
            
            frontier = frontier + 1
            
            
        A[final],A[frontier]=A[frontier],A[final]    
        
        return final
        

     
        
        