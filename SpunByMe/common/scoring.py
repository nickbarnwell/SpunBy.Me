import math

def _confidence(ups, downs):
	n = ups + downs

	if n == 0:
		return 0

	z = 1.0
	phat = float(ups) / n
	return math.sqrt(phat+z*z/(2*n)-z*((phat*(1-phat)+z*z/(4*n))/n))/(1+z*z/n)

def confidence(ups, downs):
	if ups + downs == 0:
		return 0
	else:
		_confidence(ups, downs)
		return _confidence(ups, downs)
