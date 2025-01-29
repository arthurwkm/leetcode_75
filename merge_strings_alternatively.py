
def mergeAlternately(word1, word2):
    finalword = ""
    if len(word1) > len(word2):
        for count, letter in enumerate(word1):
            if count < len(word2):
                finalword = finalword + word1[count]
                finalword = finalword + word2[count]
            else:
                finalword = finalword+ word1[count:len(word1)]
                break
    else:  
        for count, letter in enumerate(word2):
            if count < len(word1):
                finalword = finalword+ word1[count] 
                finalword = finalword+ word2[count] 
            else:
                finalword = finalword+ word2[count:len(word2)]
                break

    return finalword
    
print(mergeAlternately("abc", "pqr"))
print(mergeAlternately("ab", "pqrs"))
print(mergeAlternately("abcd", "pq"))