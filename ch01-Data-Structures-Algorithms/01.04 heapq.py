import heapq

nums = [1, 8, 2, 23, 7, -4, 18, 23, 42, 37, 2]
print(heapq.nlargest(3, nums)) # -> [42, 37, 23]
print(heapq.nsmallest(3, nums)) # -> [-4, 1, 2]

# ----------------------------------------

print(max(nums)) # -> 42
print(min(nums)) # -> -4

# ----------------------------------------

stocks = [
    {'name': 'IBM', 'shares': 100, 'price': 91.1},
    {'name': 'AAPL', 'shares': 50, 'price': 543.22},
    {'name': 'FB', 'shares': 200, 'price': 21.09},
    {'name': 'HPQ', 'shares': 35, 'price': 31.75},
    {'name': 'YHOO', 'shares': 45, 'price': 16.35}
    ]
cheap = heapq.nsmallest(1, stocks, key=lambda s: s['price'])
print('cheap->', cheap)
expensive = heapq.nlargest(2, stocks, key=lambda s: s['price'])
print('expensive->', expensive)

