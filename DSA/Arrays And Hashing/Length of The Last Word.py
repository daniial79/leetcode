def length_of_last_word_v1(s: str) -> int:
    return len(s.split()[-1])



def length_of_last_word_v2(s: str) -> int:
    SPACE_ASCII = 32
    length = 0
    
    i = -1
    
    # skipping all space characters from end of string
    while s[i] != chr(SPACE_ASCII):
        i -= 1
        
    # count length of the last word
    try:
        while s[i] != chr(SPACE_ASCII):
            length += 1
            i -= 1
    except:
        pass
    
    return length