nums1 = [1,2,3,4] 

def runningSum(nums):
    sum_array = []
    for i in range(len(nums)):
        sum_array.append(sum(nums[:i+1]))
        
    return sum_array

print(runningSum(nums1))
