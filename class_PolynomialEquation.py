import re as re
from utils import printer, fractionResult
from calculDelta import posDelta, negatifDelta, zeroDelta


class PolynomialEquationSolver:
	def __init__(self, equation):
		self.equation = equation


	def parse(self):
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
			
			# match = re.match(r'^(\d*\.?\d*)\*?X?x?(?:\^(\d+))?$', term) #Previous regex (doesn't handle whitespaces)
			match = re.match(r'^\s*(\d*\.?\d*)\s*\*?\s*X?x?(?:\^(\d+))?\s*$', term)
			if match:
				coef_str, power_str = match.groups()
				
				if not coef_str and ('X' in term or 'x' in term):
					coef_str = '1'
				elif not coef_str:
					coef_str = '0'
				
				if not power_str:
					power = '1' if ('X' in term or 'x' in term) else '0'
				else:
					power = power_str
				
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
		last_power = int(max(self.coef.keys()))

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
			print("Not a polynomial equation")