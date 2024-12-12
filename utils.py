from class_PolynomialEquation import PolynomialEquationSolver

def format_term(coef, power, term=True):
	if coef == 0:
		return ""
	if coef < 0 and term == True:
		return f"- {-coef} * X^{power} "
	if term == True:
		return f"+ {coef} * X^{power} "
	return f"{coef} * X^{power} "

def printer(left: "PolynomialEquationSolver", right: "PolynomialEquationSolver"):
	left_terms = []
	term = False
	for power, coef in left.coef.items():
		str = format_term(coef, int(power), term)
		if str:
			left_terms.append(str)
			term = True

	right_terms = []
	term = False
	for power, coef in right.coef.items():
		str = format_term(coef, int(power), term)
		if str:
			right_terms.append(str)
			term = True

	left_equation = ''.join(left_terms).strip()
	right_equation = ''.join(right_terms).strip()

	if not left_equation and not right_equation:
		print("0 = 0")
	elif not left_equation:
		print(f"0 = {right_equation}")
	elif not right_equation:
		print(f"{left_equation} = 0")
	else:
		print(f"{left_equation} = {right_equation}")
	print("")


def fractionResult(numerator, denominator):
	def gcd(a, b):
		"""
		Function to find the greatest common divisor
		eg: 51 and 45 can be divided by 3
		"""
		while b:
			a, b = b, a % b
		return a

	if denominator == 0:
		raise ValueError("Denominator cannot be zero")

	sign = 1
	if numerator * denominator < 0:
		sign = -1

	numerator = abs(numerator)
	denominator = abs(denominator)

	divisor = gcd(numerator, denominator)

	reduced_numerator = sign * (numerator // divisor)
	reduced_denominator = denominator // divisor

	print("The fractional result is:")
	return (f"{reduced_numerator}/{reduced_denominator}")