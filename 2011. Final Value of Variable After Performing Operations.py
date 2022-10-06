operations1 = ["++X","++X","X++"]

def finalValueAfterOperations(operations):
    x = 0
    for item in operations:
        if item == "--X" or item =="X--":
            x-=1

        else:
            x+=1
    
    return x

print(finalValueAfterOperations(operations1))
