def productExceptSelf(nums):
    factor = 1
    response = []

    i = len(nums)-1
    while i>=0:
        if i<len(nums)-1:
            factor = factor * nums[i+1]
        response.append(factor)
        i-=1
        
    response = list(reversed(response))

    factor = 1

    for i, n in enumerate(nums):
        if i>0:
            factor = factor * nums[i-1]
        response[i] = response[i]*factor
 

    return response

print(productExceptSelf([1,2,3,4]))
print(productExceptSelf([-1,1,0,-3,3]))