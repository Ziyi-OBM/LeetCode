class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}
        for i in range(len(nums)):
            complement = target - nums[i]      
            if dic.get(complement) != None:
                return [i,dic.get(complement)]
            dic[nums[i]]=i;