address1 = "1.1.1.1"

def defangIPaddr(s):
    s_new =""
    for char in s:

        if char == '.':
            s_new +="[.]"
        else:
            s_new += char
    
    return s_new



    





print(defangIPaddr(address1))