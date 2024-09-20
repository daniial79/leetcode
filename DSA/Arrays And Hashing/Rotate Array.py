def rotate(nums: list[int], k: int) -> None:
    """
    Do not return anything, modify nums in-place instead.
    """

    n = len(nums)
    k = k % n
    
    # use slicing [:] notation to accessing the underlying data of nums not it's pointer
    nums[:] = nums[-k:] + nums[:-k]
        
    