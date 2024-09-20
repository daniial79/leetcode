def max_area(height: list[int]) -> int:
    l, r = 0, len(height) - 1
    maximum_area = 0
    
    while l < r:
        area = min(height[l], height[r]) * (r - l)
        maximum_area = max(maximum_area, area)
        
        if height[l] < height[r]:
            l += 1
        else: 
            r -=1
        
    return maximum_area
