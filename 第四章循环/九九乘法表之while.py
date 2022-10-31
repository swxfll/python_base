x = 1
while x <= 9:
    y = 1
    while y <= x:
        print(f"{y}*{x}={x*y}\t", end='')
        y += 1
    x += 1
    print()

