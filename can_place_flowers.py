def canPlaceFlowers(flowerbed, n):
    for count, p in enumerate(flowerbed):
        if p == 0:
            if len(flowerbed) == 1:
                flowerbed[count] = 1
                n = n-1
            elif (count == 0):
                if (flowerbed[count+1] == 0):
                    flowerbed[count] = 1
                    n = n-1
            elif (count == len(flowerbed)-1): 
                if (flowerbed[count-1] == 0):
                    flowerbed[count] = 1
                    n = n-1
            else:
                if (flowerbed[count-1] == 0) & (flowerbed[count+1] == 0):
                    flowerbed[count] = 1
                    n = n-1
        if n==0:
            break
    
    if n==0:
        return True
    else: 
        return False
    
print(canPlaceFlowers([1, 0, 0, 0, 1], 1))
print(canPlaceFlowers([1, 0, 0, 0, 1], 2))
print(canPlaceFlowers([1, 0, 0, 0, 1, 0, 0], 2))