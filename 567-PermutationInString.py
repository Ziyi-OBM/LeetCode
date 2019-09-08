# Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1. 
# In other words, one of the first string's permutations is the substring of the second string.

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        l1=len(s1)
        l2=len(s2)
        s1Map={}
        window={}
        count=0
        
        if len(s1)>len(s2):
            return False
        
        #Add the substring into a mao
        for n in s1:
            if not (n in s1Map):
                s1Map[n]=1
            else: 
                s1Map[n]=s1Map[n]+1
        #Get the number of letters we need to match their frequencies       
        freqCt=len(s1Map)
        
        #Initially, insert the letters in the first window
        for i in range(l1):        
            if (s2[i] in s1Map) and (not (s2[i] in window)):
                window[s2[i]]=1
            elif s2[i] in s1Map: 
                window[s2[i]]=window[s2[i]]+1
        #Initiallize frequencies in the first window
        for keys in s1Map:
            if (keys in window) and s1Map[keys]==window[keys]:
                count = count+1
                
        #Check if completed        
        if count == freqCt:
            return True
        
        #If not, slide the window      
        for i in range(l1,l2):   
            #Look at the letter on the right end that goes into the window
            if (s2[i] in s1Map):#Only intereted in letters in the substring
                #If its a new letter not yet in the 'window' hashmap, insert it
                if not s2[i] in window:
                    window[s2[i]]=1  
                #Otherwise increase its frequency by 1    
                else:
                    window[s2[i]]=window[s2[i]]+1
                    #If the letter already matches the frequencies, adding 1 creates a mismatch, count-- 
                    if window[s2[i]]-1==s1Map[s2[i]]: 
                        count = count -1    
                #If increasing by one matches the frequency, count++    
                if window[s2[i]]==s1Map[s2[i]]:
                    count = count+1
            #Now look at the left end of the window
            
            if (s2[i-l1] in s1Map):
                #Decrease the frequency
                window[s2[i-l1]]=window[s2[i-l1]]-1
                #Not need to check for insertion this time
                #If substracting freq by 1 creates a mismatch, count--
                if (window[s2[i-l1]]+1) == s1Map[s2[i-l1]]:                
                    count = count-1
                #If substraacting freq by 1 creates a match, count++
                if (window[s2[i-l1]]) == s1Map[s2[i-l1]]:                
                    count = count+1
            #Everytime slidin the window, check if the number of matched letters
            if count == freqCt:
                return True
        #Unable to find window position that creates a match, return false.    
        return False    