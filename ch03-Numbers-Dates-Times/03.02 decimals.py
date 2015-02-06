a = 4.2
b = 2.1
print(a + b)  # 6.300000000000001 and not 6.3
print(a + b == 6.3)  # False

from decimal import Decimal
a = Decimal('4.2')
b = Decimal('2.1')
print(a + b)  # 6.3
print(a + b == 6.3)  # False
print(a + b == Decimal('6.3'))  # True
print(Decimal(6.3))  # 6.299999xxx


from decimal import *
a = Decimal('1.3')
b = Decimal('1.7')
print(a / b)  # 0.764705882xxxx
with localcontext() as lctx:
    lctx.prec = 3
    print(a / b)


with localcontext() as lctx:
    print(lctx)
    print(Decimal('1.5').__round__(0))
    print(Decimal('2.5').__round__(0))
    lctx.rounding = ROUND_HALF_UP
    print(Decimal('1.5').__round__(0))
    print(Decimal('2.5').__round__(0))

