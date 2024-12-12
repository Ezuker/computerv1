import matplotlib.pyplot as plt
import numpy as np
from utils import printer

def translateReducedForm(reducedForm, x):
	result = 0
	for power, coef in reducedForm.items():
		result += float(coef) * x** float(power)
	return result


def graphicDisplay(reducedForm, result):
	if len(result) == 2:
		x = np.linspace(result[0] + (result[0] / 5), result[1] + (result[1] / 5), 400)
	elif len(result) == 1:
		x = np.linspace(result[0] - (result[0] / 5), result[0] + (result[0] / 5), 400)
	else:
		return

	y = translateReducedForm(reducedForm, x)

	plt.plot(x, y, label=f'{printer(reducedForm, {"0": 0.0})}')
	for point in result:
		plt.scatter(point, translateReducedForm(reducedForm, point), color='red')

	plt.xlabel('x')
	plt.ylabel('y')
	plt.title(f'Plot of the quadratic function {printer(reducedForm, {"0": 0.0})}')
	plt.legend()
	plt.grid(True)
	plt.show()