def findAltitude(gain):
    max_altitude = 0
    sum = 0

    for n in gain:
        sum = sum + n
        if max_altitude<sum:
            max_altitude = sum
        
    return max_altitude

print(findAltitude([-5,1,5,0,-7]))
print(findAltitude([-4,-3,-2,-1,4,3,2]))