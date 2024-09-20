def majority_element(nums: list[int]) -> int:
    for element in set(nums):
        if element > len(nums) // 2:
            return element