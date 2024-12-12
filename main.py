import sys as sys
import re as re
from math import sqrt
from utils import printer, fractionResult


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
	numerator = (-coef.get('1', 0) - sqrt(delta))
	denominator = (2 * coef.get('2', 0))
	print(f"{-coef.get('1', 0)} / {denominator} + (sqrt({delta}) / {denominator}) * i")
	print(f"{-coef.get('1', 0)} / {denominator} - (sqrt({delta}) / {denominator}) * i")



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
		for power, coef in otherSide.coef.items():
			selfcoef = self.coef.get(power, 0)
			self.coef[power] = selfcoef - coef
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
				negatifDelta(self.coef, delta)
			elif delta == 0:
				zeroDelta(self.coef, delta)
			else:
				posDelta(self.coef, delta)
		elif last_power == 1:
			print("Polynomial degree: 1")
			print("The solution is :")
			x = self.coef.get('0', 0) / -self.coef.get('1', 0)
			print(f"{x}")
			if (x % 1 != 0):
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