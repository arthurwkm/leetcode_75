def countOcurrences(nums):
    nums_dict = {}
    occurences_dict = {}

    for n in nums:
        if n not in nums_dict.keys():
            nums_dict[n] = 1
        else:
            nums_dict[n] += 1
    
    for n in nums_dict:
        if nums_dict[n] not in occurences_dict.keys():
            occurences_dict[nums_dict[n]] = 1
        else:
            return False
        
    return True
    
print(countOcurrences([1,2,2,1,1,3]))
print(countOcurrences([1,2]))
print(countOcurrences([-3,0,1,-3,1,1,1,-3,10,0]))

    