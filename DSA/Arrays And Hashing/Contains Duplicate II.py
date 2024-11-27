def contains_nearby_duplicate(nums: list[int], k: int) -> bool:
    bucket = dict()

    for index, value in enumerate(nums):
        # check for equal values
        if value in bucket:
            
            # check for differentiation
            if index - bucket[value] <= k:
                return True
            
            # update the pair
        bucket[value] = index
            
    return False
