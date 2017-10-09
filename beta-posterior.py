#! /usr/bin/env python

import sys
import os
import math
import random
import argparse
import unittest
import logging
from scipy.stats import beta, binom

logging.basicConfig(format='%(levelname)s: %(message)s', level=logging.DEBUG)
_LOG = logging.getLogger(os.path.basename(__file__))

underflow_limit = math.log(sys.float_info.min) * 1.00001
overflow_limit = math.log(sys.float_info.max) * 0.99999


class BinomialModel(object):
    """
    A class for demonstrating Bayesian statistics with a binomial sampling
    distribution and a conjugate beta prior.

    >>> m = BinomialModel(seed = 111, number_of_flips = 100, probability_of_heads = 0.1)
    >>> m.n
    100
    >>> m.p
    0.1
    >>> abs(m.rectangular_integration_of_posterior(1000) - m.get_log_marginal_likelihood()) < 0.0001
    True
    """

    def __init__(self,
            seed,
            number_of_flips = 1000,
            probability_of_heads = None,
            prior_beta_a = 1.0,
            prior_beta_b = 1.0):
        self.seed = seed
        self.rng = random.Random()
        self.rng.seed(self.seed)

        self.n = number_of_flips
        self.beta_a = prior_beta_a
        self.beta_b = prior_beta_b
        self.prior_lower = 0.0
        self.prior_upper = 1.0
        self.power = 1.0

        self.beta_prior = beta(self.beta_a, self.beta_b)
        self.p = probability_of_heads
        if self.p is None:
            self.p = self.draw_p_from_prior()
        self.binomial_likelihood = binom(self.n, self.p)
        self.k = self.simulate_number_of_heads()
        self.beta_posterior = beta(
                self.beta_a + self.k,
                self.beta_b + (self.n - self.k))
    
    def _get_random_state(self):
        return self.rng.randint(1, 999999999)

    def draw_p_from_prior(self):
        return self.beta_prior.rvs(random_state = self._get_random_state())

    def simulate_number_of_heads(self):
        return self.binomial_likelihood.rvs(
                random_state = self._get_random_state())

    def get_prior_pdf(self, p = None):
        if p is None:
            p = self.p
        return self.beta_prior.pdf(p)

    def get_prior_logpdf(self, p = None):
        if p is None:
            p = self.p
        return self.beta_prior.logpdf(p)

    def get_posterior_pdf(self, p = None):
        if p is None:
            p = self.p
        return self.beta_posterior.pdf(p)

    def get_posterior_logpdf(self, p = None):
        if p is None:
            p = self.p
        return self.beta_posterior.logpdf(p)

    def get_likelihood(self, p = None):
        if p is None:
            p = self.p
        return binom.pmf(k = self.k, n = self.n, p = p)

    def get_log_likelihood(self, p = None):
        if p is None:
            p = self.p
        return binom.logpmf(k = self.k, n = self.n, p = p)

    def get_log_marginal_likelihood(self):
        return (self.get_log_likelihood() + self.get_prior_logpdf() -
                self.get_posterior_logpdf())

    def rectangular_integration_of_posterior(self, number_of_steps):
        step_size = (self.prior_upper - self.prior_lower) / number_of_steps
        position = self.prior_lower
        ln_areas = []
        while position < self.prior_upper:
            if (position + step_size) > self.prior_upper:
                step_size = self.prior_upper - position
            midpoint = position + (step_size / 2.0)
            ln_density = (self.get_log_likelihood(p = midpoint) +
                    self.get_prior_logpdf(p = midpoint))
            ln_slice_area = math.log(step_size) + ln_density 
            ln_areas.append(ln_slice_area)
            position += step_size
        assert ((len(ln_areas) == number_of_steps) or
                (len(ln_areas) == number_of_steps + 1)), (
                "unexpected number of steps {0}".format(len(ln_areas)))
        mean_ln_area = sum(ln_areas) / len(ln_areas)
        # Reduce underflow by shifting all log areas before exponentiating
        # ln_scale = max(underflow_limit - l for l in ln_areas)
        ln_scale = -mean_ln_area 
        scaled_ln_areas = [lna + ln_scale for lna in ln_areas]
        overflow_scale_used = False
        if max(scaled_ln_areas) >= overflow_limit:
            _LOG.debug("Using overflow scaling for rectangular integration")
            overflow_scale_used = True
            ln_scale = min(overflow_limit - l for l in ln_areas)
            scaled_ln_areas = [lna + ln_scale for lna in ln_areas]
        try:
            scaled_areas = [math.exp(lna) for lna in scaled_ln_areas]
        except OverflowError as e:
            _LOG.warn("Overflow at math.exp(lna)\n"
                    "lna = {lna}\n"
                    "ln_scale = {ln_scale}\n"
                    "overflow scale? {overflow_scale_used}".format(
                        lna = lna,
                        ln_scale = ln_scale,
                        overflow_scale_used = overflow_scale_used))
            raise
        scaled_ml = sum(scaled_areas)
        # Shift the log marginal likelihood back
        ln_ml = math.log(scaled_ml) - ln_scale 
        return ln_ml


def arg_is_positive_int(i):
    try:
        if int(i) < 1:
            raise
    except:
        msg = '{0!r} is not a positive integer'.format(i)
        raise argparse.ArgumentTypeError(msg)
    return int(i)

def arg_is_positive_float(i):
    try:
        if float(i) <= 0.0:
            raise
    except:
        msg = '{0!r} is not a positive real number'.format(i)
        raise argparse.ArgumentTypeError(msg)
    return float(i)

def arg_is_nonnegative_float(i):
    try:
        if float(i) < 0.0:
            raise
    except:
        msg = '{0!r} is not a non-negative real number'.format(i)
        raise argparse.ArgumentTypeError(msg)
    return float(i)


def main_cli(argv = sys.argv):
    parser = argparse.ArgumentParser()

    parser.add_argument('-n', '--number-of-flips',
            action = 'store',
            type = arg_is_positive_int,
            default = 1000,
            help = 'Number of coin flips.')
    parser.add_argument('-p', '--probability-of-heads',
            action = 'store',
            type = arg_is_nonnegative_float,
            default = 0.5,
            help = 'Probability of any coin flip landing heads up.')
    parser.add_argument('-a', '--beta-prior-alpha',
            action = 'store',
            type = arg_is_positive_float,
            default = 1.0,
            help = ('Value of the alpha parameter of the beta prior on the '
                    'probability of heads.'))
    parser.add_argument('-b', '--beta-prior-beta',
            action = 'store',
            type = arg_is_positive_float,
            default = 1.0,
            help = ('Value of the beta parameter of the beta prior on the '
                    'probability of heads.'))
    parser.add_argument('seed',
            metavar='SEED',
            type = arg_is_positive_int,
            help = 'Seed for random number generator.')

    if argv == sys.argv:
        args = parser.parse_args()
    else:
        args = parser.parse_args(argv)

    m = BinomialModel(seed = args.seed,
            number_of_flips = args.number_of_flips,
            probability_of_heads = args.probability_of_heads,
            prior_beta_a = args.beta_prior_alpha,
            prior_beta_b = args.beta_prior_beta)
    ln_ml = m.get_log_marginal_likelihood()
    sys.stdout.write("Log marginal likelihood: {0}\n".format(ln_ml))

if __name__ == "__main__":
    if "--run-tests" in sys.argv:

        sys.stderr.write("""
*********************************************************************
Running test suite using the following Python executable and version:
{0}
{1}
*********************************************************************
\n""".format(sys.executable, sys.version))

        import doctest

        # doctest.testmod(verbose = True)
        suite = unittest.TestSuite()
        suite.addTest(doctest.DocTestSuite())

        tests = unittest.defaultTestLoader.loadTestsFromName(
               os.path.splitext(os.path.basename(__file__))[0])
        suite.addTests(tests)

        runner = unittest.TextTestRunner(verbosity = 2)
        runner.run(suite)

        sys.exit(0)

    main_cli()
