nums1 = [2,7,11,15]
target1 =9

def threeSum(nums, target):
    index_1 , index_2 = 0, len(nums) -1

    while index_1  < index_2:

        if nums[index_1] + nums[index_2] == target:
            return[index_1+1, index_2+1]
        elif nums[index_2] > target:
            index_2 -= 1
        elif nums[index_1] + nums[index_2] < target:
            index_1 += 1
        else:
            index_2 -=1
    
    return [-1,-1]

print(threeSum(nums1, target1))
