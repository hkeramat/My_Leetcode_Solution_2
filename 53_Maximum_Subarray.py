nums1 = [-2,1,-3,4,-1,2,1,-5,4]

def maxSubArray(nums):
    max_subassary = current_subarray = nums[0]
    for num in nums[1:]:
        current_subarray = max(num, num + current_subarray)

        max_subassary = max( current_subarray, max_subassary)
    
    return max_subassary
    

print(maxSubArray(nums1))
