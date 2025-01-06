import re as re
from utils import printer, fractionResult
from calculDelta import posDelta, negatifDelta, zeroDelta


class PolynomialEquationSolver:
	def __init__(self, equation):
		self.equation = equation


	def parse(self):
		"""
		Parse the mathematical equation into structured coefficients.
		Converts equation to terms, handles various input formats, and extracts coefficients by their power.
		"""
		self.equation = self.equation.replace('-', "+-")
		self.terms = self.equation.split("+")
		print(self.terms)
		self.coef = {}
		for idx, term in enumerate(self.terms):
			if not term.strip() or term.strip() == "-":
				if idx == 0:
					continue
				raise ValueError("Please, provide a good prompt")
			
			sign = 1
			if term.startswith('-'):
				sign = -1
				term = term[1:]
			
			# match = re.match(r'^(\d*\.?\d*)\*?X?x?(?:\^(\d+))?$', term) #Previous regex (doesn't handle whitespaces)
			match = re.match(r'^\s*(\d*\.?/?\d*)\s*(\*?)\s*X?x?(?:\^(\d+))?\s*$', term)
			if match:
				coef_str, sign_term, power_str = match.groups()
				
				if not coef_str and ('X' in term or 'x' in term) and not sign_term:
					coef_str = '1'
				elif not coef_str and not sign_term:
					coef_str = '0'
				
				if not power_str:
					power = '1' if ('X' in term or 'x' in term) else '0'
				else:
					power = power_str

				if coef_str.__contains__("/"):
					deno, nume = coef_str.split("/")
					coef_str = float(deno) / float(nume)
				
				coefficient = float(coef_str) * sign
				self.coef[power] = self.coef.get(power, 0) + coefficient
			else:
				raise ValueError("Please, provide a good prompt")


	def reductionForm(self, otherSide: "PolynomialEquationSolver"):
		"""
		Substract the left side by the right side.
		Returns the reduced left side 
		"""
		nb_step = 0
		print(f"Equation :")
		print(f"{printer(self.coef, otherSide.coef)}", end="\n\n")
		for power, coef in otherSide.coef.items():
			selfcoef = self.coef.get(power, 0)
			self.coef[power] = selfcoef - coef
			if power in otherSide.coef:
				otherSide.coef[power] = 0
				nb_step = nb_step + 1
				print(f"Reduce form step {nb_step}")
				print(f"{printer(self.coef, otherSide.coef)}", end="\n\n")
		return self.coef


	def calculDelta(self):
		"""
		Determine the polynomial degree, calcul the delta
		Return the result as a list
		"""
		self.coef = {power: coef for power, coef in self.coef.items() if coef != 0}
		if len(self.coef) == 0:
			print("Each real number is a solution")
			return None
		last_power = int(max(map(int, self.coef.keys())))

		if last_power > 2:
			print(f"Polynomial degree: {last_power}")
			print(f"The polynomial degree is strictly greater than 2, I can't solve.")
			return None
		
		if last_power == 2:
			print("Polynomial degree: 2")
			delta = self.coef.get('1', 0) ** 2 - 4 * self.coef.get('2', 0) * self.coef.get('0', 0)
			result = []
			if delta < 0:
				result = negatifDelta(self.coef, delta)
			elif delta == 0:
				result = zeroDelta(self.coef, delta)
			else:
				result = posDelta(self.coef, delta)
			return result
		elif last_power == 1:
			print("Polynomial degree: 1")
			print("The solution is :")
			x = self.coef.get('0', 0) / -self.coef.get('1', 0)
			print(f"x1 : {x}")
			if (x % 1 != 0):
				print(f"{fractionResult(self.coef.get('0', 0), -self.coef.get('1', 0))}")
			return [x]
		else:
			print("Error: Not a polynomial equation (and possibly impossible)")
			return None