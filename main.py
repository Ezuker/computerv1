import sys as sys
from class_PolynomialEquation import PolynomialEquationSolver
from graphic import graphicDisplay

def main():
	try:
		left, right = sys.argv[1].split("=")
	except ValueError as e:
		print(f"Prompt must have 2 sides (example):", file=sys.stderr)
		print("\"1 * X^1 = 5\"", file=sys.stderr)
		return
	except IndexError as e:
		print(f"Prompt must have 2 sides (example):", file=sys.stderr)
		print("\"1 * X^1 = 5\"", file=sys.stderr)
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
		print(f"Error {e}", file=sys.stderr)


if __name__ == '__main__':
	main()