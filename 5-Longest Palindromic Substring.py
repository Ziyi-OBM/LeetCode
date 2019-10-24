class Solution:
    def longestPalindrome(self, s: str) -> str:
        if not s:
            return ""
        n=len(s)
        length=1
        longest = s[0]
        
        table=[[0 for i in range(n)] for j in range(n)]
        #Initialize the case of 1 and 2 letter palindrome, and we can deduce the rest
        for i in range(n):
            table[i][i]=1
        for i in range(n-1):
            if s[i]==s[i+1]:
                table[i][i+1]=1
                longest=s[i:i+2]
        #Rule: a word s[i:j] if palindron if and only if :
        #the word s[i+1:j-1] is palindron AND s[i]==s[j]
        #because the answer build on [i+1][j-1], use j(end cursor) as outter loop so that all rows in col j-1 
        #s[:][j-1]are already computed. 
        for j in range(2,n):
            for i in range(0,j):
                if s[i]==s[j] and table[i+1][j-1]:
                    table[i][j]=1
                    if j-i>length:
                        length=j-i
                        longest=s[i:j+1]
        
                    
        return longest