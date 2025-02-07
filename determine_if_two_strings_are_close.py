def determineIfClose(word1, word2):
    if len(word1) != len(word2):
        return False
    
    w1 = {}
    w2 = {}

    for i in word1:
        if i in w1:
            w1[i] += 1
        else:
            w1[i] = 1

    for i in word2:
        if i in w2:
            w2[i] += 1
        else:
            w2[i] = 1

    if w1 == w2: 
        return True
    elif w1.keys() != w2.keys():
        return False
    else:
        occurencies1 = {}
        occurencies2 = {}

        for i in w1:
            if w1[i] in occurencies1:
                occurencies1[w1[i]] += 1
            else:
                occurencies1[w1[i]] = 1

        for i in w2:
            if w2[i] in occurencies2:
                occurencies2[w2[i]] += 1
            else:
                occurencies2[w2[i]] = 1

        if occurencies1 == occurencies2:
            return True
        else:
            return False
    
    



print(determineIfClose("abbzzca", "babzzcz"))
print(determineIfClose("a", "aa"))
print(determineIfClose("cabbba", "abbccc"))