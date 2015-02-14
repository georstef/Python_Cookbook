from fractions import Fraction
f = Fraction(3,5)
print(f)  # κλάσμα
print(f.numerator)  # αριθμητής
print(f.denominator)  # παρονομαστής
print(f * 4)  # 3*4 / 5
print(f * Fraction(1,2))  # 3/5 * 1/2
print(f + Fraction(1,5))  # 3/5 + 1/5
print(float(f))  # as float
print(f.limit_denominator(3))  # limits denominator (keeps numerator as int)

x = 0.75
y = Fraction(*x.as_integer_ratio())
print(y)  # 3/4
