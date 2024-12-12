import sys as sys
import re as re
from math import sqrt


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

	# Calculate the GCD
	divisor = gcd(numerator, denominator)
	print(f"divisor {divisor}")
	print(f"numerator {numerator}")
	print(f"denominator {denominator}")

	# Reduce the fraction
	reduced_numerator = sign * (numerator // divisor)
	reduced_denominator = denominator // divisor
	print(f"reduced nume {reduced_numerator}")
	print(f"reduced deno {reduced_denominator}")

	print("The fractional result is:")
	return (f"{reduced_numerator}/{reduced_denominator}")

class PolynomialEquationSolver:
	def __init__(self, equation):
		self.equation = equation


	def parse(self):
		self.equation = self.equation.replace(' ','')
		self.equation = self.equation.replace('-', "+-")
		self.terms = self.equation.split("+")
		self.coef = {}
		for term in self.terms:
			if not term:
				continue
			
			sign = 1
			if term.startswith('-'):
				sign = -1
				term = term[1:]
			
			match = re.match(r'^(\d*\.?\d*)\*?X?(?:\^(\d+))?$', term)
			if match:
				coef_str, power_str = match.groups()
				
				# Gestion du coefficient
				if not coef_str and 'X' in term:
					coef_str = '1'
				elif not coef_str:
					coef_str = '0'
				
				# Gestion de la puissance
				if not power_str:
					power = '1' if 'X' in term else '0'
				else:
					power = power_str
				
				# Conversion et ajout
				coefficient = float(coef_str) * sign
				self.coef[power] = self.coef.get(power, 0) + coefficient
			else:
				raise ValueError("Please, provide a good prompt")


	def reductionForm(self, otherSide: "PolynomialEquationSolver"):
		nb_step = 0
		print(f"Equation :")
		printer(self, otherSide)
		for power, coef in self.coef.items():
			other_coef = otherSide.coef.get(power, 0)
			self.coef[power] = coef - other_coef
			if power in otherSide.coef:
				otherSide.coef[power] = 0
				nb_step = nb_step + 1
				print(f"Reduce form step {nb_step}")
				printer(self, otherSide)

	


	def calculDelta(self):
		self.coef = {power: coef for power, coef in self.coef.items() if coef != 0}
		if len(self.coef) == 0:
			print("Each real number is a solution")
			return
		last_power = int(max(self.coef.keys()))  # Gets the highest power
		if last_power > 2:
			print(f"Polynomial degree: {last_power}")
			print(f"The polynomial degree is strictly greater than 2, I can't solve.")
			return
		if last_power == 2:
			print("Polynomial degree: 2")
			delta = self.coef.get('1', 0) ** 2 - 4 * self.coef.get('2', 0) * self.coef.get('0', 0)
			if delta < 0:
				print("The discriminant is negative")
				print("The equation doesn't have reel solutions")
			elif delta == 0:
				print("The discriminant is equal to 0")
				print("There is one solution:")
				print(f"x : {-self.coef.get('1', 0) / (self.coef.get('2', 0) * 2)}")
			else:
				print("The discriminant is positive")
				print("There is two solutions:")
				print(f"x1 : {(-self.coef.get('1', 0) + sqrt(delta)) / (2 * self.coef.get('2', 0))}")
				print(f"x2 : {(-self.coef.get('1', 0) - sqrt(delta)) / (2 * self.coef.get('2', 0))}")
				print(f"{fractionResult((-self.coef.get('1', 0) + sqrt(delta)), (2 * self.coef.get('2', 0)))}")
				print(f"{fractionResult((-self.coef.get('1', 0) - sqrt(delta)), (2 * self.coef.get('2', 0)))}")

		elif last_power == 1:
			print("Polynomial degree: 1")
			print("The solution is :")
			print(f"{self.coef.get('0', 0) / -self.coef.get('1', 0)}")
			print(f"{fractionResult(self.coef.get('0', 0), -self.coef.get('1', 0))}")
		else:
			print("Please provide a polynomial equation")


def main():
	try:
		left, right = sys.argv[1].split("=")
		left = PolynomialEquationSolver(left.strip())
		right = PolynomialEquationSolver(right.strip())
		left.parse()
		right.parse()
		left.reductionForm(right)
		left.calculDelta()
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()