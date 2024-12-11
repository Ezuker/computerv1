import sys as sys
from re import findall
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


class PolynomialEquationSolver:
	def __init__(self, equation):
		self.equation = equation


	def parse(self):
		self.terms = findall(r'([+-]?\s*\d*\.?\d*)\s*\*?\s*X\^?(\d*)', self.equation)
		self.coef = {}
		for term in self.terms:
			self.coef[term[1].replace(" ", "")] = float(term[0].replace(" ", ""))
		

	def reductionForm(self, otherSide: "PolynomialEquationSolver"):
		nb_step = 1
		print(f"Reduce form step {nb_step}")
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
		last_item = int(list(self.coef.items())[-1][0])
		if last_item > 2:
			print(f"Polynomial degree: {last_item}")
			print(f"The polynomial degree is strictly greater than 2, I can't solve.")
			return
		if last_item == 2:
			print("Polynomial degree: 2")
			delta = self.coef['1'] ** 2 - 4 * self.coef['2'] * self.coef['0']
			if delta < 0:
				print("The discriminant is negative")
				print("The equation doesn't have reel solutions")
			elif delta == 0:
				print("The discriminant is equal to 0")
				print("There is one solution:")
				print(f"x : {-self.coef['1'] / (self.coef['2'] * 2)}")
			else:
				print("The discriminant is positive")
				print("There is two solutions:")
				print(f"x1 : {(-self.coef['1'] + sqrt(delta)) / (2 * self.coef['2'])}")
				print(f"x2 : {(-self.coef['1'] - sqrt(delta)) / (2 * self.coef['2'])}")
		elif last_item == 1:
			print("Polynomial degree: 1")
			print("The solution is :")
			print(f"{self.coef['0'] / -self.coef['1']}")
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