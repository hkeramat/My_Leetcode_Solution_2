class Solution:
    def validPalindrome(self, s: str) -> bool:
        i , j = 0, len(s) -1
        count = 0
    
        def check_polindrom(s,i,j):
            while i < j:
                if s[i]!= s[j]:
                    return False
        
                i+=1
                j-=1
            return True

        while i < j:
            if s[i] != s[j]:
                return check_polindrom(s, i, j - 1) or check_polindrom(s, i + 1, j)


            i+=1
            j-=1

        return True 