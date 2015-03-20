def tvm():
	"""
	Concepts from CFA Level I Time Value of Money:
		PV: pv_f, pv_perp
		FV 
		EAR
		HPR: hpr, hpr_cfr
		BDY
		HPY
		EAY
		MMY: mmy_hpy, mmy_bdy
	"""

# present value
def pv_f(fv, r, n):
	"""Returns present value given future value, rate, periods compounding."""
	present_value = [fv, r, n]
	return fv / (1 + r) ** n

# effective annual rate
def ear(r, m):
	# r is the stated rate, m is the number of periods compounding.
	"""Returns effective annual rate given stated rate, periods compounding."""
	effective_annual_rate = [r, m]
	return (1 + r/m) ** m - 1

def ear_cont(r):
	import math
	return math.exp(r) - 1

# present value of a perpetuity
def pv_perp(pmt, r):
	# pmt is the period payment, r is the discount rate.
	"""Returns present value of perpetuity given payment, rate."""
	present_value_perp = [pmt, r]
	return pmt / r

# future value
def fv_p(pv, r, n):
	"""Returns future value given present value, rate, periods compounding."""
	future_value = [pv, r, n]
	return pv * (1 + r) ** n

# holding period return
def hpr(ev, bv):
	# ev is ending value, bv is beginning value.
	"""Returns holding period return given ending value, beginning value."""
	holding_period_return = [ev, bv]
	return ev / bv - 1

# holding period return with interim cash flow received
def hpr_cfr(ev, bv, cfr):
	# cfr is interim cash flow received, e.g. a dividend.
	"""
	Returns holding period return given ending value, \
		beginning value, interim cash flow received."""
	holding_period_return_cfr = [ev, bv, cfr]
	return (ev + cfr) / bv - 1

# bank discount yield of Treasury bills, assuming 360 days per year
def bdy(D, F, t):
	"""
	Returns Treasury bill bank discount yield given \
		annualized yield on a bank discount basis, \
		dollar discount (difference between face value and purchase price), \
		face value (par value) of bill.
	"""
	bank_discount_yield = [D, F, t]
	# D = diff between face value and purchase price
	# F = face value (par value) of bill
	# t = days until maturity 
	return (D / F) * (360 / t)

# holding period yield of a fixed income instrument.
def hpy(p1, p0, D1):
	"""
	Returns holding period yield of an instrument given \
		initial price, price received at maturity, \
		interest payment (distrubution).
	"""
	holding_period_yield = [p1, p0, D1]
	# p0 = initial price
	# p1 = price received at maturity
	# D1 = interest payment
	return (p1 + D1) / p0 - 1

# effective annual yield, assuming 365 days per year
def eay(hpy, t):
	"""
	Returns effective annual yield given \
		holding period yield, days until maturity.
	"""
	# t = days to maturity
	effective_annual_yield = [hpy, t]
	return (1 + hpy) ** (365 / t) - 1

# money market yield or CD equivalent yield
def mmy_hpy(hpy, t):
	"""
	Returns money market yield given holding period yield,\
		days until maturity.
	"""
	# t = days remaining until maturity
	money_market_yield_hpy = [hpy, t]
	return hpy * (360 / t)

def mmy_bdy(bdy, t):
	"""
	Returns money market yield given bank discount yield, \
		days until maturity.
	"""
	money_market_yield_bdy = [bdy, t]
	return (360 * bdy) / (360 - t * bdy)

# Coming soon:
# def mwr():
# def twr():
