def maxOperations(nums, k):
    operations = 0
    nums.sort()
    left = 0
    right = len(nums)-1

    while left<right:
        sum = nums[left]+nums[right]
        if sum == k:
            operations+=1
            left+=1
            right -=1
        elif sum<k:
            left +=1
        else:
            right -=1

    return operations 

#print(maxOperations(nums = [1,2,3,4], k = 5))
#print(maxOperations(nums = [3,1,3,4,3], k = 6))
print(maxOperations([2,1,3,4,7], 5))