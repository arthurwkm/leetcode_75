def maxSubarray(letters, k):
    start = 0
    stop = k-1
    current_v = 0
    max_v = 0
    for i in range(0,k):
        if letters[i] in "aeiou":
            current_v+=1
    max_v = current_v

    while stop<len(letters)-1:
        if letters[stop+1] in "aeiou":
            current_v +=1
        if letters[start] in "aeiou":
            current_v -=1

        if max_v < current_v:
            max_v = current_v
        start +=1
        stop +=1
    
    return max_v

print(maxSubarray(letters = "abciiidef", k = 3))
print(maxSubarray(letters = "aeiou", k = 2))
print(maxSubarray(letters = "leetcode", k = 3))