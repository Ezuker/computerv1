from math import sqrt
from utils import fractionResult

def posDelta(coef, delta):
	print("The discriminant is positive")
	print("There is two solutions:")

	x1 = (-coef.get('1', 0) + sqrt(delta)) / (2 * coef.get('2', 0))
	x2 = (-coef.get('1', 0) - sqrt(delta)) / (2 * coef.get('2', 0))
	print(f"x1 : {x1}")
	print(f"x2 : {x2}")
	if (x1 % 1 != 0):
		print(f"{fractionResult((-coef.get('1', 0) + sqrt(delta)), (2 * coef.get('2', 0)))}")
	if (x2 % 1 != 0):
		print(f"{fractionResult((-coef.get('1', 0) - sqrt(delta)), (2 * coef.get('2', 0)))}")


def zeroDelta(coef, delta):
	print("The discriminant is equal to 0")
	print("There is one solution:")

	x = -coef.get('1', 0) / (coef.get('2', 0) * 2)
	print(f"x : {x}")
	if (x % 1 != 0):
		print(f"{fractionResult(-coef.get('1', 0), (coef.get('2', 0) * 2))}")


def negatifDelta(coef, delta):
	print("The discriminant is negative")
	print("There is two complex solutions")
	delta = -delta
	denominator = (2 * coef.get('2', 0))
	print(f"{-coef.get('1', 0)} / {denominator} + (sqrt({delta}) / {denominator}) * i")
	print(f"{-coef.get('1', 0)} / {denominator} - (sqrt({delta}) / {denominator}) * i")