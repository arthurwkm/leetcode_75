def reverseVowels(s):
    s = list(s)
    vs = 'aeiouAEIOU' 
    v = [] #vowels
    vp = [] #vowels positions
    for i, c in enumerate(s):
        if c in vs: #if char is vowel
            v.append(c) #append c to v and pos to vp
            vp.append(i)
    
    v = reversed(v)
    for i, c in enumerate(v):
        s[vp[i]] = c

    return ''.join(s)

print(reverseVowels('leetcode'))
print(reverseVowels('IceCreAm'))