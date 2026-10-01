#ex1
import math

r = float(input("Enter circle radius? "))
area = math.pi * (r ** 2)
print(f"Circle area = {area:.1f}")

#ex2
celsius = float(input("Enter the temperature in Celsius? "))
fahrenheit = (celsius * 9 / 5) + 32
print(f"{int(celsius)} (C) = {fahrenheit:.1f} (F)")

#ex3
n = int(input("Enter a number? "))

if n < 2:
    is_prime = False
else:
    is_prime = True
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            is_prime = False
            break

if is_prime:
    print(f"{n} is a prime number")
else:
    print(f"{n} is a NOT prime number")


#ex4
n = int(input("Enter a number? "))

if n <= 0:
    print(f"{n} is a NOT perfect number")
else:
    sum_divisors = sum(i for i in range(1, n) if n % i == 0)
    if sum_divisors == n:
        print(f"{n} is a perfect number")
    else:
        print(f"{n} is a NOT perfect number")

#ex5

colors = ["Blue", "Red", "Yellow", "Black"]  
fav_color = input("What is your favorite color? ").strip()

found = False
for idx, c in enumerate(colors):
    if c.lower() == fav_color.lower():
        print(f"Your color is at index {idx} in my list")
        found = True
        break

if not found:
    print("Sorry, I could not find your color")

#ex6

range1 = list(range(0, 7))
range2 = list(range(1, 11, 3))
range3 = list(range(5, 0, -1))
range4 = list(range(6, -3, -2))

print("range1:", ", ".join(map(str, range1)))
print("range2:", ", ".join(map(str, range2)))
print("range3:", ", ".join(map(str, range3)))
print("range4:", ", ".join(map(str, range4)))

#ex7

def remove_dollar_sign(s):
    return s.replace("$", "")

#ex8
def extract_even(l):
    return [x for x in l if x % 2 == 0]

#ex9

def factorial(n):
    if n < 0:
        return None
    res = 1
    for i in range(1, n + 1):
        res *= i
    return res

#ex10

def get_divisors(n):
    n = abs(n)
    if n == 0:
        return []
    return [i for i in range(1, n + 1) if n % i == 0]

#ex11

import math

x1 = float(input("Enter x1: "))
y1 = float(input("Enter y1: "))
x2 = float(input("Enter x2: "))
y2 = float(input("Enter y2: "))

distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
print(f"Distance = {distance}")

#ex12

def print_pattern(m, n):
    for i in range(m):
        for j in range(n):
            if i == 0 or i == m - 1 or j == 0 or j == n - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
        print()