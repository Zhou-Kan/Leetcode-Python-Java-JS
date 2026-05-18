def climb_stairs(n: int) -> int:
    if n < 0:
        raise Exception("It's not a valid number")
    
    if n <= 2:
        return n
    # first is the result of the first stair, and the second is the result of the second stair
    first, second = 1, 2

    # to find out the result of the last stair 
    for _ in range(2, n):
        first, second = second, first + second

    return second

print(climb_stairs(3))
print(climb_stairs(0))
print(climb_stairs(1))
print(climb_stairs(-1))