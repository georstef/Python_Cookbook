import random

values = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(random.choice(values))
print(random.choice(values))
print(random.choice(values))

print(random.sample(values, 2))
print(random.sample(values, 3))
print(random.sample(values, 4))

random.shuffle(values)
print(values)
random.shuffle(values)
print(values)

print(random.randint(10,20))  # from 10 to 20
print(random.randrange(1, 20, 2))  # from 1 to 20-1 step 2 (only odd numders)
print(random.randrange(0, 20, 2))  # from 0 to 20-1 step 2 (only even numders)
print(random.randrange(5))  # from 0 to 5-1
print(random.random())  # from 0 to 1
print(random.getrandbits(32))  # 32 random bits (or 4 bytes)


