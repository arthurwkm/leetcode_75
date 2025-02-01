def compress(chars):
    s = ""
    current_c = chars[0]
    count_c = 0
    pointer = 0
    if len(chars) == 1:
        return chars
    
    for i, c in enumerate(chars):
        print(f'current letter is {c}')
        if c != current_c:
            if count_c == 1:
                chars[pointer] = current_c
            else:
                chars[pointer:i] = [current_c] + list(str(count_c))
            print(f'counted {count_c} of letter {current_c}. will put this from {pointer} to {i}. new pointer is {i}')
            current_c = c
            count_c = 1
            pointer = i
            
        else:
            count_c +=1
        if i == len(chars)-1:
            if count_c == 1:
                chars[pointer] = current_c
            else:
                chars[pointer:i+1] = [current_c] + list(str(count_c))
            print(f'2counted {count_c} of letter {current_c}. will put this from {pointer} to {i}. new pointer is {i}')
            pointer = i

    return chars

print(compress(["a"]))
print(compress(["a","a","b","b","c","c","c"]))
print(compress(["a","b","b","b","b","b","b","b","b","b","b","b","b"]))