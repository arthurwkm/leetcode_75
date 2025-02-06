def maxConsecutiveOnes(nums, k):
    zeros_idx = []
    current_window_size = 0
    max_window_size = 0

    start = 0
    stop = k-1

    for i, n in enumerate(nums):
        if n==0:
            zeros_idx.append(i)

    if k>=len(nums) | k>len(zeros_idx):
        return len(nums)
            
    while stop<len(zeros_idx):
        if start>0:
            l = zeros_idx[start-1] + 1
        else:
            l = 0
        if stop<len(zeros_idx)-1:
            r = zeros_idx[stop+1] - 1
        else:
            r = len(nums)-1
        current_window_size = (r-l) + 1

        if max_window_size<current_window_size:
            max_window_size = current_window_size

        start+=1
        stop+=1
    
    return max_window_size

print(maxConsecutiveOnes(nums = [0,0,0,1], k = 4))
print(maxConsecutiveOnes(nums = [0,0,1,1,0,0,1,1,1,0,1,1,0,0,0,1,1,1,1], k = 3))