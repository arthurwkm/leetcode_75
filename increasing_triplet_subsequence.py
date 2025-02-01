def increasingTriplet(nums):
    i= len(nums)-1
    biggest = nums[i]
    biggests = []

    smallest = nums[0]
    smallests = []
    
    biggest = nums[i]
    while i>=0:
        if nums[i] > biggest:
            biggest = nums[i]
        
        biggests.append(biggest)
        i-=1

    biggests = list(reversed(biggests))
    
    for n in nums:
        if n<smallest:
            smallest = n
        
        smallests.append(smallest)

    for i, n in enumerate(nums):
        if (n>smallests[i]) & (n<biggests[i]):
            return True

    return False

print(increasingTriplet([6,1,2, 5,4, 0]))