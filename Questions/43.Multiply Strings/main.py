def multiply(num1: str, num2: str) -> str:
    # 234
    #  45
    # =>  432
    #.    54  => 20 15 10 16 12 8
    #   1170
    #.  936
    #.  10530
    if num1 == '0' or num2 == '0':
        return '0'
    
    m, n = len(num1), len(num2)
    pos = [0] * (m + n)

    for i in range(m - 1, -1, -1):
        for j in range(n - 1, -1, -1):
            num = int(num1[i]) * int(num2[j]) + pos[i + j + 1]
            pos[i + j + 1] = num % 10
            pos[i + j] += num // 10

    start = 0
    while start < m + n and pos[start] == 0:
        start += 1


    return ''.join(map(str, pos[start:]))

print(multiply('99', '99'))
print(multiply('2', '22'))
print(multiply('0', '0'))

