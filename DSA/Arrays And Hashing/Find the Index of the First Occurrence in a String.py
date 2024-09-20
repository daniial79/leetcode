def str_str_v0(haystack: str, needle: str) -> int:
    for indicator in range(len(haystack)):
        
        if haystack[indicator] != needle[0]:
            continue


        scout = 0
        while scout < len(needle):
            
            try:

                if needle[scout] != haystack[indicator:][scout]:
                    break

                scout += 1
                if scout == len(needle):
                    return indicator
            
            except IndexError:
                break
            
    return -1

def str_str_v1(haystack: str, needle: str) -> int:
    for i in range(len(haystack)+1-len(needle)):
        if haystack[i:i+len(needle)]==needle:
            return i
    return -1 
