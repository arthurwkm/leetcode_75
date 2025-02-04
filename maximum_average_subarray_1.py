def maxSubarray(nums, k):
    start = 0
    stop = k-1
    avg = 0
    for i in range(0,k):
        avg = avg + nums[i]
    avg = avg/k
    max_avg = avg

    while stop<len(nums)-1:
        avg = (avg - nums[start]/k) + nums[stop+1]/k
        if max_avg < avg:
            max_avg = avg
        start +=1
        stop +=1
    
    return max_avg

print(maxSubarray(nums = [1,12,-5,-6,50,3], k = 4))
print(maxSubarray(nums = [5], k = 1))