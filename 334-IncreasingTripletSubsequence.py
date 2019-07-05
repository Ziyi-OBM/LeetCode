class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        if len(nums)<3:
            return False
        
        subseq=[0,0,0]
        subseq[0]=nums[0]
        cursor=0
        
        for i in range(1,len(nums)):
            for k in reversed(range(cursor+1)):
                if nums[i]>subseq[k]:
                    subseq[k+1]=nums[i]
                    if k+1>cursor:
                        cursor=k+1
                    break                   
                elif k==0:
                    subseq[k]=nums[i]
            if cursor == 2:
                return True
  
        return False

# this is junchao editing trick
                
