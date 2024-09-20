def remove_element(nums: list[int], val: int) -> int:
    
    # Count occurence of val inside nums
    occurence = 0
    for scout in nums:
        
        if scout == val:
            occurence += 1
            
    # Remove the val from nums using remove mutator method for occurence-th time
    for _ in range(occurence):
        nums.remove(val)
        
    # Return other elements quantity
    return len(nums)
        
    