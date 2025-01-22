#!/usr/bin/env python3
'''
func uses the scipy library to calculate the beta
cumulative distribution function
'''
from scipy import special


def posterior(x, n, p1, p2):
    """
    func calculates the posterior probability of obtaining the data
    """
    if not isinstance(n, int) or n <= 0:
        raise ValueError("n must be a positive integer")
    if not isinstance(x, int) or x < 0:
        raise ValueError(
                "x must be an integer that is greater than or equal to 0"
                )
    if x > n:
        raise ValueError("x cannot be greater than n")
    if not isinstance(p1, float) or not 0 <= p1 <= 1:
        raise ValueError("p1 must be a float in the range [0, 1]")
    if not isinstance(p2, float) or not 0 <= p2 <= 1:
        raise ValueError("p2 must be a float in the range [0, 1]")
    if p2 <= p1:
        raise ValueError("p2 must be greater than p1")
    beta_cdf_p1 = special.btdtr(x + 1, n - x + 1, p1)
    beta_cdf_p2 = special.btdtr(x + 1, n - x + 1, p2)
    posterior_prob = beta_cdf_p2 - beta_cdf_p1
    return posterior_prob
