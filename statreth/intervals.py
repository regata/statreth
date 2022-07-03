import numpy as np


def hdi(samples, mass):
    """Estimates Highest Density Interval (HDI) for an array of `samples` for a given probability `mass`
    The HDI is the minimum width Bayesian credible interval (BCI).
    Note: it asssumes that the underlying distribution is unimodal
    """
    # number of samples included in HDI
    n_inc = int(mass * len(samples))
    # number of possible intervals
    n_intervals = len(samples) - n_inc
    # sort samples asc
    samples = np.sort(samples)
    # interval widths
    # widths = np.zeros((n_intervals,))
    # for i in range(n_intervals):
    #     widths[i] = samples[i + n_inc] - samples[i]
    widths = samples[n_inc:] - samples[:n_intervals]
    # take the interval that has the minimum width, i.e. highest density
    min_idx = widths.argmin()
    hdi_min = samples[min_idx]
    hdi_max = samples[min_idx + n_inc]
    return [hdi_min, hdi_max]


def pi(samples, mass):
    """Computes Percentile Interval for an array of `samples`"""
    low = (1 - mass) / 2
    high = 1 - low
    return [np.quantile(samples, low), np.quantile(samples, high)]