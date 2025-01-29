def kidsWithCandies(candies, extraCandies):
    j = 0
    for i in candies:
        if i>j:
            j = i
    print(j)
    k = []
    for i in candies:
        if (i+extraCandies) >= j:
            k.append("true")
        else:
            k.append("false")
    return k

print(kidsWithCandies([12,1,12], 10))