def is_happy(n: int) -> bool:

    tracker: list[int] = [square_sum(n)]

    while tracker[-1] != 1:
        new_number = square_sum(tracker[-1])
        
        if new_number in tracker:
            return False
            
        tracker.append(new_number)


    return True


def square_sum(n: int) -> int:
    result: int = 0

    while n > 0:
        result += (n % 10) ** 2
        n //= 10

    return result