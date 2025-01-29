def reverseWords(s): 
    word = []
    words = []
    for i, c in enumerate(s):
        if len(word) == 0:
            if s[i] != ' ':
                word.append(c)
        else:
            if s[i] == ' ': #if word is open, close the word after finding space
                words.append(''.join(word))
                word = []
            else:
                word.append(c)
    
    #if word was not closed (there was no trailing space), close it
    if len(word)!= 0:
        words.append(''.join(word))

    rwords = []
    for i, w in enumerate(words):
        rwords.append(words[-(i+1)])

    return ' '.join(rwords)

print(reverseWords("  hello world  "))
print(reverseWords("the sky is blue"))
print(reverseWords("a good   example"))