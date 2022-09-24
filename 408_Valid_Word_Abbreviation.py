class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs)==1:
            return strs[0]
        
        def twoCom(common_sofar, next):
            two_common_prefix =""
            for i in range (min(len(common_sofar), len(next))):
                if common_sofar[i] == next[i]:
                    two_common_prefix+= next[i]
                else:
                    break
    
            return two_common_prefix

    
        common_prefix = twoCom(strs[0],strs[1])

        for i in range(2, len(strs)):
            common_prefix = twoCom(common_prefix, strs[i])
        
        

        return(common_prefix)