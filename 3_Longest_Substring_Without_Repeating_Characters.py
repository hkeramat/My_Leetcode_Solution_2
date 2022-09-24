class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        
        ans = []                         # saves length of the substring in each visit
        substring = ""                   # a substring from s
        i = 0                            # counter for each visit
        
        while i < len(s):
            
            if s[i] in substring:
                
                substring = substring[1:]# if character of the visit in substring, then remove the first character of the substring 
                
            else:
                
                substring += s[i]
                i+=1
            
            ans.append(len(substring))   # add length of the substring to the ans
    
        if s == substring:               # in s does not have repeating characters 
            return len(s)
    
        return max(ans)                  #return maximum length of the substrings saved in ans