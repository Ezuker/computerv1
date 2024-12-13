from utils import fractionResult

def sqrt(x):
	"""
	Function that return the sqrt of x
	"""
	last_guess= x/2.0
	while True:
		guess= (last_guess + x/last_guess)/2
		if abs(guess - last_guess) < .000001: # example threshold
			return guess
		last_guess= guess


def posDelta(coef, delta):
	"""
	Calcul the result with the positive delta method
	"""
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
		print(f"{fractionResult(-coef.get('1', 0), (coef.get('2', 0) * 2))}")
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
	x_imagpart = sqrt(delta) / denominator
	print(f"x1: {x_reelpart} + i * {x_imagpart}")
	print(f"x2: {x_reelpart} - i * {x_imagpart}")
	if (x_reelpart % 1 != 1):
		print(f"{fractionResult(-coef.get('1', 0), denominator)} + i * {x_imagpart}")
		print(f"{fractionResult(-coef.get('1', 0), denominator)} - i * {x_imagpart}")
	return None