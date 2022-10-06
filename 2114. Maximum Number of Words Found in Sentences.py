sentences = ["alice and bob love leetcode", "i think so too", "this is great thanks very much"]

def mostWordsFound(sentences):
    if not sentences:
        return 0
    max_res = 0
    for item in sentences:
        max_words = 0
        for char in item:
            if char==" ":
                max_words+=1
        
        max_res =max(max_res, max_words+1)
    
    return max_res



print(mostWordsFound(sentences))
