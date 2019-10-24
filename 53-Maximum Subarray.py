class Solution:
    
    def maxSubArray(self, nums: List[int]) -> int:
        #DP solution
        if not nums:
            return 0
        # At each element, decide if we start new or continue previous
        # dp=[nums[0]]     
        # for i in range(1,len(nums)):
        #     dp.append(max(nums[i],dp[i-1]+nums[i]))        
        # return max(dp)
        
        #Improved dp with O(1) space
        #Since we're only using dp[i-1], just let dp := dp[i-1] in the previous case
        dp=nums[0]    
        dpmax=nums[0]
        for i in range(1,len(nums)):
            dp=max(nums[i],dp+nums[i])   
            dpmax=max(dpmax,dp)
        return dpmax

    
#     #D&C solution
#     def maxSubArray(self, nums: List[int]) -> int:
#         return self.findMax(nums,0,len(nums)-1)
#    
#     #Similar to quick sort partition, but devide to 3 possible situations and choose max
#     #The max subarray is 1.completely on the left 2. completely on the right 3.Include the pivot element
#     def findMax(self,nums,i,j):
#         if i==j:
#             return nums[i]        
#         mid= (j+i)//2
#        
#         return max(self.findMax(nums,i,mid),self.findMax(nums,mid+1,j),self.findCross(nums,i,j))
#            
#     def findCross(self,nums,i,j):
#         #Start from middle go two sides   
#         mid= (j+i)//2
#         lmax=nums[mid]
#         rmax=nums[mid]
#         ltotal=nums[mid]
#         rtotal=nums[mid]
#        
#         for x in reversed(range(i,mid)):
#             ltotal=ltotal+nums[x]
#             if ltotal>=lmax:
#                 lmax=ltotal
#                
#         for x in range(mid+1,j+1):
#             rtotal=rtotal+nums[x]
#             if rtotal>=rmax:
#                 rmax=rtotal
# 
#         return lmax+rmax-nums[mid]
                
            
            
        
        
        