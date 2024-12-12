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
	x_reelpart = -coef.get('1', 0) / denominator
	x_imagpart = sqrt(delta) / denominator
	print(f"x1: {x_reelpart} + i * {x_imagpart}")
	print(f"x2: {x_reelpart} - i * {x_imagpart}")
	if (x_reelpart % 1 != 1):
		print(f"{fractionResult(-coef.get('1', 0), denominator)} + i * {x_imagpart}")
		print(f"{fractionResult(-coef.get('1', 0), denominator)} - i * {x_imagpart}")