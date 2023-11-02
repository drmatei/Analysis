from tabulate import tabulate
import math

og_length = int(input("Enter a starting length for the sum: "))
p = int(input("Enter a number of additions for positive numbers: "))
q = int(input("Enter a number of additions for negative numbers: "))
list = []
j = 0

# This structure calculates the sum the "normal" way
for _ in range(0, 4):
    n = og_length * (2 ** j)
    i = 1
    sign = 1
    result = float(0)
    while i <= n:
        result = result + 1 / i * sign
        sign = sign * (-1)
        i = i + 1
    list.append(result)
    j += 1

headers = ["n", "p", "q", "solution", "exponential sol"]

table = [
    [og_length, 0, 0, list[0], math.exp(list[0])],
    [og_length * 2, 0, 0, list[1], math.exp(list[1])],
    [og_length * 4, 0, 0, list[2], math.exp(list[2])],
    [og_length * 8, 0, 0, list[3], math.exp(list[3])],
]


# This structure calculates the sum with the changes to the order of summation
k = 0
for _ in range(0, 4):
    n = og_length * (2 ** k)
    result = float(0)
    i = 0
    j = 1
    while 2*i+1 < n and 2*j < n:
        i1 = 0
        while i1 < p and 2*i+1 < n:
            result = result + 1/(2*i+1)
            i1 = i1 + 1
            i = i + 1
        j1 = 0
        while j1 < q and j*2 < n:
            result = result - 1/(2*j)
            j1 = j1 + 1
            j = j + 1
    table.append([n, p, q, result, math.exp(result)])
    k += 1

print(tabulate(table, headers=headers, tablefmt="grid"))
