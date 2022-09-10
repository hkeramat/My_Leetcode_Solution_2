l1 = [3,1,5,2]
def findSmallestElement(l):
    smallestElement = l[0]
    smallestIndex   = 0
    for i in range(1, len(l)):
        if l[i] < smallestElement:
            smallestElement = l[i]
            smallestIndex   = 0
    
    print(smallestElement)

if __name__ =="__main__":
    findSmallestElement(l1)
