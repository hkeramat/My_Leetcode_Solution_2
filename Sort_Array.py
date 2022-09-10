l1 = [3,7,1,5,8,2,8,6,9,4]
def findSmallestElement(l):
    smallestElement = l[0]
    smallestIndex   = 0
    for i in range(1, len(l)):
        if l[i] < smallestElement:
            smallestElement = l[i]
            smallestIndex   = i
    return(smallestIndex)
    
def selectionSort(l):
    new_arr = []
    for i in range (len(l)):
        smallest = findSmallestElement(l)
        a = l.pop(smallest)
        new_arr.append(a)
    return(new_arr)

print(selectionSort(l1))


    
