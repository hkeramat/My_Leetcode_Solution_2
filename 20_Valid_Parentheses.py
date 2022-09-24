class Solution(object):
    def isValid(self,s): 
        dict = {
    '(': ')', '{': '}', '[' :']',
}
        open_par = []
        for char in s:
            if char in dict:
                open_par.append(char)
            elif open_par and dict[open_par[-1]] == char:
                open_par.pop()
            else:
                return False
        
        return not open_par
