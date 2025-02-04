def moveZeroes(nums):
    i = 0
    not_sorted = True
    if nums[0] == 0:
        zeron = 1
    else:
        zeron  = 0
        
    while not_sorted:
        if i<len(nums)-1:
            if nums[i+1] == 0:
                zeron += 1
            else:
                temp = nums[i+1]
                nums[i+1] = nums[i]
                nums[(i-zeron) + 1] = temp
        else:
            not_sorted = False

        i+=1
    


        

    return nums



print(moveZeroes([0,1,0,3,12]))