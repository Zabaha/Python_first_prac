import math

x = 51

a = (x ** 3 - 83 * x ** 6 + 33) / (math.sin(x ** 3 - x ** 5) + x ** 3)
b = (38 * x ** 5 + 69 * x ** 8 - 36)/(math.sin(x) - x ** 4)
c = 14 * x ** 8 - math.fabs(x)
result = a - b - c
print(f"{result:.2e}")

x = 202

if x < 131:
    result = x ** 3 - 83 * x ** 6 + 33
    print(f"{result:.2e}")
elif 131 <= x < 147:
    result = math.sin(x ** 3 - x ** 5) + x ** 3
    print(f"{result:.2e}")
elif x >= 147:
    result = x ** 6 - x ** 3
    print(f"{result:.2e}")


def func(n, m):
    sum_a1 = 0
    sum_a2 = 0
    for i in range(1, n + 1):
        for j in range(1, m + 1):
            a = j + j ** 4
            sum_a1 += a
            sum_a2 += sum_a1

    a_fin = sum_a2 / 61

    sum_b = 0
    for i in range(1, n + 1):
        b = (i ** 5 / 47) + i ** 8
        sum_b += b
    b_fin = 83 * sum_b
    return a_fin - b_fin


print(f"{func(38, 28):.2e}")


def rec(n):
    if n == 0:
        return 6
    if n == 1:
        return 2
    a = rec(n - 1)
    return (1/91) * a + (1/41) * a ** 2


print(f"{rec(16):.2e}")
