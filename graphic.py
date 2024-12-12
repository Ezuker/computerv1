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
		x = np.linspace(result[0] - (result[0] / 10), result[1] + (result[1] / 10), 400)
	elif len(result) == 1:
		x = np.linspace(result[0] - (result[0] / 10), result[0] + (result[0] / 10), 400)  # 400 points between -10 and 10
	else:
		return

	# Calculate the corresponding y values
	y = translateReducedForm(reducedForm, x)

	# Create the plot
	plt.plot(x, y, label=f'{printer(reducedForm, {"0": 0.0})}')

	for point in result:
		plt.scatter(point, translateReducedForm(reducedForm, point), color='red')


	# Add labels and title
	plt.xlabel('x')
	plt.ylabel('y')
	plt.title(f'Plot of the quadratic function {printer(reducedForm, {"0": 0.0})}')

	# Add a legend
	plt.legend()

	# Show the plot
	plt.grid(True)
	plt.show()