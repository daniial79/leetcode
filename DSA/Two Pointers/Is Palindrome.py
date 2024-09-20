def is_palindrome(s: str) -> bool:
    
    left, right = 0, len(s) - 1
    
    
    while left < right:
        
        if not s[left].isalnum():
            left += 1
            continue
        
        if not s[right].isalnum():
            right -= 1
            continue
        
        if s[left] != s[right]:
            return False
        
    return True