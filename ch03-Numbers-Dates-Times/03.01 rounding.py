# built-in round function always rounds to nearest even number
print(round(1.5))  # 2
print(round(2.5))  # 2

print(round(1.15, 1))  # 1.1
print(round(1.16, 1))  # 1.2
print(round(2.25, 1))  # 2.2


print(round(12345, -1))  # 12340
print(round(12346, -1))  # 12350

# careful
print(4.2 + 2.1)  # 6.300000000000001 and not 6.3
