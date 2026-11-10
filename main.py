import math

a = float(input("Введіть катет a: "))
b = float(input("Введіть катет b: "))
expected_c = float(input("Введіть очікувану гіпотенузу: "))

c = math.sqrt(a ** 2 + b ** 2)
perimeter = a + b + c

check = abs(c - expected_c) < 1e-6

print(f"Гіпотенуза: {c}, Периметр: {perimeter}, Збігається: {check}")