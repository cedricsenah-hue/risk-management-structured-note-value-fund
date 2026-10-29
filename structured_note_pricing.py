"""
Pricing of a principal-protected structured note on the S&P 500.

Product: 1-year note sold at USD 1,000. At maturity the investor receives
1,000 + 25% x max(S&P 500 return, 0) x 1,000.

Replication (bank's hedge):
    long 1 zero-coupon bond, face value 1,000, maturity 1 year
    long 0.25 European at-the-money call (S = K = 1,000, T = 1)

Inputs (as of end of December 2024, see report for sources):
    risk-free rate  : 4.20% per year (13-week US T-Bill, ^IRX), i.e. ln(1.042) continuous
    dividend yield  : 1.26% per year (S&P 500)
    volatility      : 13.08% (1-year annualised historical volatility of daily S&P 500 returns)
"""

from math import exp, log, sqrt
from statistics import NormalDist

N = NormalDist().cdf

NOTE_PRICE = 1_000.0
PARTICIPATION = 0.25
S = K = 1_000.0
T = 1.0
R_ANNUAL = 0.0420
R = log(1 + R_ANNUAL)          # continuous compounding (about 4.11%)
Q = 0.0126                     # dividend yield
SIGMA = 0.1308


def bsm_call(s, k, t, r, q, sigma):
    """Black-Scholes-Merton price of a European call with continuous dividend yield."""
    d1 = (log(s / k) + (r - q + 0.5 * sigma**2) * t) / (sigma * sqrt(t))
    d2 = d1 - sigma * sqrt(t)
    price = s * exp(-q * t) * N(d1) - k * exp(-r * t) * N(d2)
    delta = exp(-q * t) * N(d1)
    return price, d1, d2, delta


def historical_volatility(prices, window=252):
    """Annualised volatility of daily returns over the last `window` observations.

    `prices` must be a chronologically sorted list of closing levels.
    Note: the result is a decimal (0.13 = 13%), not a percentage.
    """
    rets = [prices[i] / prices[i - 1] - 1 for i in range(1, len(prices))][-window:]
    mean = sum(rets) / len(rets)
    var = sum((x - mean) ** 2 for x in rets) / (len(rets) - 1)
    return sqrt(var) * sqrt(252)


if __name__ == "__main__":
    call, d1, d2, delta = bsm_call(S, K, T, R, Q, SIGMA)
    embedded_option = PARTICIPATION * call
    bond = NOTE_PRICE / (1 + R_ANNUAL) ** T
    cost = bond + embedded_option
    margin = NOTE_PRICE - cost

    print(f"d1 = {d1:.3f}, d2 = {d2:.3f}, delta = {delta:.3f}")
    print(f"ATM call (1 unit)        : {call:8.2f} USD")
    print(f"Embedded option (0.25x)  : {embedded_option:8.2f} USD")
    print(f"Zero-coupon bond         : {bond:8.2f} USD")
    print(f"Total replication cost   : {cost:8.2f} USD")
    print(f"Bank margin              : {margin:8.2f} USD ({margin / NOTE_PRICE:.2%})")
    # Maximum participation the bank could offer with zero margin
    print(f"Break-even participation : {(NOTE_PRICE - bond) / call:.1%}")
