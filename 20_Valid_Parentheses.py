dict = {
    '(': ')', '{': '}', '[' :']',
}

s1 = "]"

def isValid(s):
    open_par = []

    for char in s:
        if char in dict:
            open_par.append(char)
        elif open_par and dict[open_par[-1]] == char:
            open_par.pop()
        else:
            return False
    if open_par:
        return False
    return True


print(isValid(s1))
