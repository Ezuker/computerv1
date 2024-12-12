import sys as sys
from class_PolynomialEquation import PolynomialEquationSolver
from graphic import graphicDisplay

def main():
	try:
		left, right = sys.argv[1].split("=")
	except ValueError as e:
		print(f"Prompt must have 2 sides (example):")
		print("\"1 * X^1 = 5\"")
		return
	try:
		left = PolynomialEquationSolver(left.strip())
		right = PolynomialEquationSolver(right.strip())
		left.parse()
		right.parse()
		reducedForm = left.reductionForm(right)
		result = left.calculDelta()
		if result:
			graphicDisplay(reducedForm, result)
	except Exception as e:
		print(e)


if __name__ == '__main__':
	main()