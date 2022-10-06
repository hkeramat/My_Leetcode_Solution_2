height = [1,8,6,2,5,4,8,3,7]

def maxArea(height):
    max_area = 0
    right = len(height) -1
    left = 0
    while left < right:

        width = right - left
        if height[right] > height[left]:
            area =   height[left] * width 
            left+=1 
        else:
            area = height[right] * width 
            right -=1

        max_area = max(area, max_area)  
         
    return max_area

print(maxArea(height))
