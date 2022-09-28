nums = [8,1,2,2,3]

def smallerNumbersThanCurrent(nums):
    nums_copy = nums
    sorted_nums = sorted(nums)
    return [sorted_nums.index(nums_copy[i]) for i in range(len(nums))]
   

print(smallerNumbersThanCurrent(nums))
