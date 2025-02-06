def findPivot(nums):
    t_sum = 0
    l_sum = 0
    r_sum = 0

    for n in nums:
        t_sum += n

    for i, n in enumerate(nums):
        if i>0:
            l_sum+=nums[i-1]
        r_sum = t_sum-n-l_sum
        print(f'l: {l_sum}, n: {n}, r: {r_sum}')
        if l_sum == r_sum:
            return i
    return -1

print(findPivot([1,7,3,6,5,6]))
print(findPivot([1,2,3]))
print(findPivot([2,1,-1]))