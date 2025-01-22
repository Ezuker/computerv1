from utils import fractionResult


def float_round(value):
	mod = value % 0.01
	if mod > 0.0050:
		return 0.01 - mod + value
	else:
		return value - mod


def posDelta(coef, delta):
	"""
	Calcul the result with the positive delta method
	"""
	print("The discriminant is positive")
	print("There is two solutions:")

	x1 = (-coef.get('1', 0) + (delta ** 0.5)) / (2 * coef.get('2', 0))
	x2 = (-coef.get('1', 0) - (delta ** 0.5)) / (2 * coef.get('2', 0))
	print(f"x1 : {x1}")
	print(f"x2 : {x2}")
	if (x1 % 1 != 0):
		print(f" x1 : {fractionResult((-coef.get('1', 0) + (delta ** 0.5)), (2 * coef.get('2', 0)))}")
	if (x2 % 1 != 0):
		print(f" x2 : {fractionResult((-coef.get('1', 0) - (delta ** 0.5)), (2 * coef.get('2', 0)))}")
	return [x1, x2]


def zeroDelta(coef, delta):
	"""
	Calcul the result with the zero delta method
	"""
	print("The discriminant is equal to 0")
	print("There is one solution:")

	x = -coef.get('1', 0) / (coef.get('2', 0) * 2)
	print(f"x1 : {x}")
	if (x % 1 != 0):
		print(f" x1 : {fractionResult(-coef.get('1', 0), (coef.get('2', 0) * 2))}")
	return [x]


def negatifDelta(coef, delta):
	"""
	Calcul the result with the negative delta method
	"""
	print("The discriminant is negative")
	print("There is two complex solutions")
	delta = -delta
	denominator = (2 * coef.get('2', 0))
	x_reelpart = -coef.get('1', 0) / denominator
	x_imagpart = (delta ** 0.5) / denominator
	print(f"x1: {(x_reelpart)} + i * {(x_imagpart)}")
	print(f"x2: {(x_reelpart)} - i * {(x_imagpart)}")
	if (x_reelpart % 1 != 1):
		frac_img = fractionResult((delta ** 0.5), denominator)
		print(f" x1 : {fractionResult(-coef.get('1', 0), denominator)} + i * {frac_img}")
		print(f" x2 : {fractionResult(-coef.get('1', 0), denominator)} - i * {frac_img}")
	return None