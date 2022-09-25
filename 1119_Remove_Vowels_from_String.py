s_test = "leetcodeisacommunityforcoders"

def removeVowels(s):
    vowels = 'aeiou'
    s_new =""
    for char in s:

        if char not in vowels:
            s_new += char
        

    
    return s_new



    





print(removeVowels(s_test))