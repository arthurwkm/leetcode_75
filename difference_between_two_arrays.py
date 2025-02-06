def difference(nums1, nums2):
    hashm = {}
    nums1_only = []
    nums2_only = []

    for i, n in enumerate(nums1):
        if nums1[i] not in hashm.keys():
            hashm[nums1[i]] = [1]
        else:
            if 1 not in hashm[nums1[i]]:
                hashm[nums1[i]].append(1) 

    for i, n in enumerate(nums2):
        if nums2[i] not in hashm.keys():
            hashm[nums2[i]] = [2]
        else:
            if 2 not in hashm[nums2[i]]:
                hashm[nums2[i]].append(2) 


    for key in hashm:
        if (1 in hashm[key]) & (2 not in hashm[key]):
            nums1_only.append(key)
        elif (2 in hashm[key]) & (1 not in hashm[key]):
            nums2_only.append(key)

    return [nums1_only, nums2_only]

print(difference(nums1 = [1,2,3], nums2 = [2,4,6]))
print(difference(nums1 = [1,2,3,3], nums2 = [1,1,2,2]))