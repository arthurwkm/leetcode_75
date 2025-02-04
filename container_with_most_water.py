def maxArea(height):
    max_value = 0 
    left = 0
    right = len(height)-1
    while left<right:
        if height[left]< height[right]:
            wall = height[left]
            area = (right-left)*wall
            left+=1
        else:
            wall = height[right]
            area = (right-left)*wall
            right-=1
        
        if area > max_value:
            max_value = area


    return max_value

print(maxArea([1,8,6,2,5,4,8,3,7]))
print(maxArea([1,1]))