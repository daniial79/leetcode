def remove_duplicates(nums: list[int]) -> int:
    
    for indicator in range(len(nums)):

        scout: int = indicator + 1

        try:
            
            while nums[scout] == nums[indicator]:
                del nums[indicator]

        
        except IndexError:
            break

    return len(nums)
