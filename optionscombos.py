from sympy import Symbol, Piecewise, solve
from sympy.plotting import plot
from typing import List, Tuple
from spb import *


x = Symbol("x")


def buy_opt_call(strike: float, price: float, contract: int = 100, x: Symbol = x):
    return Piecewise((-price, x <= strike), (-price + x - strike, x > strike), (0, True))*contract


def buy_opt_put(strike: float, price: float, contract: int = 100, x: Symbol = x):
    return Piecewise((-price, x >= strike), (-price + strike - x, x < strike), (0, True))*contract


def sell_opt_call(strike: float, price: float, contract: int = 100, x: Symbol = x):
    return -buy_opt_call(strike, price, contract, x)


def sell_opt_put(strike: float, price: float, contract: int = 100, x: Symbol = x):
    return -buy_opt_put(strike, price, contract, x)


def buy_underlying(price: float, contract: int = 100, x: Symbol = x):
    return buy_opt_call(0, price, contract, x)


def sell_underlying(price: float, contract: int = 100, x: Symbol = x):
    return -buy_underlying(price, contract, x)


def buy_call_spread(strikes: Tuple[float, float], price: float, contract: int = 100, x: Symbol = x):
    # to avoid the code trying to do any annoying floating point ops,
    # pretend both of the options are free, then factor in the price at the end.
    return buy_opt_call(strikes[0], 0, contract, x) + sell_opt_call(strikes[1], 0, contract, x) - price*contract


def sell_call_spread(strikes: Tuple[float, float], price: float, contract: int = 100, x: Symbol = x):
    return -buy_call_spread(strikes, price, contract, x)


def buy_put_spread(strikes: Tuple[float, float], price: float, contract: int = 100, x: Symbol = x):
    # to avoid the code trying to do any annoying floating point ops,
    # pretend both of the options are free, then factor in the price at the end.
    return buy_opt_put(strikes[1], 0, contract, x) + sell_opt_put(strikes[0], 0, contract, x) - price*contract


def sell_put_spread(strikes: Tuple[float, float], price: float, contract: int = 100, x: Symbol = x):
    return -buy_put_spread(strikes, price, contract, x)


def buy_straddle(strike: float, price: float, contract: int = 100, x: Symbol = x):
    return buy_opt_call(strike, 0, contract, x) + buy_opt_put(strike, 0, contract, x) - price*contract


def sell_straddle(strike: float, price: float, contract: int = 100, x: Symbol = x):
    return -buy_straddle(strike, price, contract, x)


def buy_strangle(strikes: Tuple[float, float], price: float, contract: int = 100, x: Symbol = x):
    return buy_opt_call(strikes[1], 0, contract, x) + buy_opt_put(strikes[0], 0, contract, x) - price*contract


def buy_butterfly(strikes: Tuple[float, float, float], price: float, contract: int = 100, x: Symbol = x):
    return buy_opt_call(strikes[0], 0, contract, x) + 2*sell_opt_call(strikes[1], 0, contract, x) + buy_opt_call(strikes[2], 0, contract, x) - price*contract


def sell_butterfly(strikes: Tuple[float, float, float], price: float, contract: int = 100, x: Symbol = x):
    return -buy_butterfly(strikes, price, contract, x)


print(buy_butterfly((25, 30, 35), 2.50))
