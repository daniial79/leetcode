def can_construct(ransom_note: str, magazine: str) -> bool:
    alphabetFrequencyTracker = [0] * 26
    
    for i in magazine:
        alphabetFrequencyTracker[ord(i) - 65] += 1
        
    for j in ransom_note:
        alphabetFrequencyTracker[ord(j) - 65] -= 1
        
    for k in alphabetFrequencyTracker:
        if k < 0: return False
        
    return True