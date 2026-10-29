# Risk Management in Financial Markets: Structured Note and Value Fund

School project from my Master in Finance (2025), by **Cédric Senah**.

**In short:** I play the role of an analyst in a bank (a made up bank called *Winston Capital*) that wants to sell two new products. I check how much they cost, how much the bank earns, whether clients would want them and what can go wrong.

## Part A. A safe investment linked to the stock market

The client invests USD 1,000 for one year. If the S&P 500 goes up, the client gets 25% of the gain. If it goes down, the client still gets the USD 1,000 back.

* **Structure**: long a 1 year zero coupon Treasury bond (face value USD 1,000) + long 0.25 European at the money call on the S&P 500.
* **Pricing**: Black Scholes Merton with dividend yield (r = 4.20%, q = 1.26%, σ = 13.08%, T = 1).
* **Key results**

| Item | USD per note |
|---|---|
| Zero coupon bond | 959.69 |
| Embedded option (0.25 call) | 16.47 |
| Total cost | 976.16 |
| **Bank margin** | **23.84 (2.38%)** |
| Break even participation | about 61% |

* Risk analysis (pre launch market and rate risk, model and hedging risk, counterparty, liquidity, regulatory) and mitigation (locking the hedge at launch, rate hedges, static hedging, CSA collateral).

## Part B. A fund that buys cheap stocks

A fund that buys the 10% cheapest U.S. stocks compared to their book value ("value" stocks) and updates the list every month. I test it on real historical data from the [Kenneth R. French Data Library](https://mba.tuck.dartmouth.edu/pages/faculty/ken.french/data_library.html).

| Indicator (monthly) | Value |
|---|---|
| Average return | 1.32% |
| Volatility | 9.06% |
| Beta | 0.92 |
| Sharpe / Sortino | 0.116 / 0.169 |
| Jensen's alpha | about 0.42% |
| 95% VaR, parametric (USD 300m) | −40.75m |
| 99% VaR, parametric | −59.38m |
| 95% VaR, historical simulation | −35.84m |

Also covered: fee positioning (about 0.40% to 0.75% per year), risk based and behavioural explanations of the value premium, and a comparison of parametric and historical VaR.

## Files

| File | Content |
|---|---|
| `report.pdf` | Full report: case summary, method, results and discussion |
| `structured_note_pricing.py` | Python implementation of the note pricing and margin (Part A) |
| `value_fund_analysis.xlsx` | Spreadsheet with performance ratios and VaR (Part B) |

Run the pricing script (Python 3.8+, standard library only):

```bash
python structured_note_pricing.py
```

## Skills illustrated

Option replication and pricing · fixed income discounting · structured product margin analysis · risk identification and hedging · factor investing · performance measurement (Sharpe, Sortino, CAPM alpha) · parametric and historical Value at Risk · Python and Excel.

## Data sources

S&P 500 daily levels (Investing.com) · 13 week U.S. Treasury bill yield (Yahoo Finance, `^IRX`) · Kenneth R. French Data Library ("Portfolios Formed on Book to Market", "Fama/French 3 Factors").
