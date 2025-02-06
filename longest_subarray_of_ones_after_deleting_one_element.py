def longestSubarray(nums):
    zeros_idx = []
    current_window_size = 0
    max_window_size = 0

    for i, n in enumerate(nums):
        if n==0:
            zeros_idx.append(i)
    
    i = 0

    if len(zeros_idx) == 0:
        return len(nums)-1
            
    while i<len(zeros_idx):
        if i>0:
            l = zeros_idx[i-1] + 1
        else:
            l = 0
        if i<len(zeros_idx)-1:
            r = zeros_idx[i+1] - 1
        else:
            r = len(nums)-1
        current_window_size = (r-l)

        if max_window_size<current_window_size:
            max_window_size = current_window_size

        i+=1
    
    return max_window_size

print(longestSubarray(nums = [1,1, 0, 1]))
print(longestSubarray(nums = [0,1,1,1,0,1,1,0,1]))
print(longestSubarray(nums = [1,1,1]))
