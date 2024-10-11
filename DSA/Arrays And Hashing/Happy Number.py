def is_happy(n: int) -> bool:

    cache: dict[int, bool] = {}
    
    current_step = square_sum(n)
    
    while current_step != 1:
        
        if cache.get(current_step):
            return False
        
        cache[current_step] = True
        current_step = square_sum(current_step)
    
    return True


def square_sum(n: int) -> int:
    result: int = 0

    while n > 0:
        result += (n % 10) ** 2
        n //= 10

    return result