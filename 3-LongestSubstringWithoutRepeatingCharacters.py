class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest=0
        start=0
        lookup={}
        for i in range(len(s)):
            it=s[i]
            
            if lookup.get(it)!=None:
                dupId=lookup.get(it)
                for j in range(start,dupId+1):
                    lookup.pop(s[j])
                start=dupId+1
                
            lookup[it]=i
            if len(lookup)>longest:
                longest = len(lookup)
        return longest