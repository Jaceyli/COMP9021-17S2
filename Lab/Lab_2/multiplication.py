for x in range(100, 1_000):
    for y in range(10, 100):
        p = x * (y % 10)
        q = x * (y // 10)
        w = q * 10 + p
        a = p // 10 ** 3 + q // 10 ** 2 + w // 10 ** 3
        b = x // 10 ** 2 + p // 10 //10 % 10 + q // 10 % 10 + w // 10 // 10 % 10
        c = x // 10 % 10 + y // 10 + p // 10 % 10 + q % 10 + w // 10 % 10
        d = x % 10 + y % 10 + p % 10 + w % 10
        if a == b == c == d:
        	print(f'{x} * {y} = {x * y}, all columns adding up to {a}')
