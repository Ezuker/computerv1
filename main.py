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
	# Collect non-zero terms for left and right sides
	left_terms = [
		format_term(left.c, 0, term=False),
		format_term(left.b, 1, term=left.c != 0),
		format_term(left.a, 2, term=left.b != 0 or left.c != 0)
	]
	# left_terms = [term for term in left_terms if term]

	right_terms = [
		format_term(right.c, 0, term=False),
		format_term(right.b, 1, term=right.c != 0),
		format_term(right.a, 2, term=right.b != 0 or right.c != 0)
	]
	# right_terms = [term for term in right_terms if term]

	# Join the terms
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
		self.c = 0
		self.b = 0
		self.a = 0
		for term in self.terms:
			if term[1] == "0":
				self.c = float(term[0].replace(" ", ""))
			elif term[1] == "1":
				self.b = float(term[0].replace(" ", ""))
			elif term[1] == "2":
				self.a = float(term[0].replace(" ", ""))
			else:
				raise ValueError("c bon")
		

	def reductionForm(self, otherSide: "PolynomialEquationSolver"):
		printer(self, otherSide)
		self.c = self.c - otherSide.c
		otherSide.c = 0
		printer(self, otherSide)
		self.b = self.b - otherSide.b
		otherSide.b = 0
		printer(self, otherSide)
		self.a = self.a - otherSide.a
		otherSide.a = 0
		printer(self, otherSide)

	
	def calculDelta(self):
		delta = self.b ** 2 - 4 * self.a * self.c
		if delta < 0:
			print("The discriminant is negative")
			print("The equation doesn't have reel solutions")
		elif delta == 0:
			print("The discriminant is equal to 0")
			print("There is one solution:")
			print(f"x : {-self.b / (self.a * 2)}")
		else:
			print("The discriminant is positive")
			print("There is two solutions:")
			print(f"x1 : {(-self.b + sqrt(delta)) / (2 * self.a)}")
			print(f"x2 : {(-self.b - sqrt(delta)) / (2 * self.a)}")



def main():
	# try:
		left, right = sys.argv[1].split("=")
		left = PolynomialEquationSolver(left.strip())
		right = PolynomialEquationSolver(right.strip())
		left.parse()
		right.parse()
		left.reductionForm(right)
		left.calculDelta()
	# except Exception as e:
	# 	print(e)


if __name__ == '__main__':
	main()