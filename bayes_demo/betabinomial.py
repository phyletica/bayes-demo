"""Module for calculating the posterior probability distribution and marginal likelihood of a parameter from a binomial distribution using a beta prior probability distribution.

Used to compute Figure 1 in:
"Jamie R. Oaks, Kerry A. Cobb, Vladimir N. Minin, and Adam D. Leaché. 2018. Marginal likelihoods in phylogenetics: a review of methods and applications."
"""

import numpy as np
import scipy.stats as st

class BetaBinomial(object):
    """Binomial model

    Parameters:
        a: alpha parameter for beta prior distribution, defaults to 1
        b: beta parameter for beta prior distribution, defaults to 1
        n: sample size of simulated, defaults to 100
        p: proportion of successes, defaults to 0.5
        params: number of parameters to draw from probability density functions

    Examples:

        M = BetaBinomial()

        MM = BetaBinomial(a=0.5, b=0.5, n=1000, p=0.25)

        print(
            '''
            Likelihood Density = {}
            Prior Density = {}
            Posterior Density = {}
            Marginal Likelihood = {}
            '''.format(MM.like, MM.prior, MM.post, MM.marginal)
        )

    Attributes:
        a: alpha shape parameter of model
        b: beta shape parameter of model
        n: sample size of model
        p: proportion success of model
        x: array between 0 and 1 with length given by params argument
        like_df: likelihood density function of array x
        prior_df: prior probability density function of array x
        post_df: posterior probability density function of array x
        like: model likelihood
        prior: model prior probability
        post: model posterior probability
        marginal: model marginal likelihood

    Methods:
        update()

    Returns: Binomial model computed from a beta prior

    """

    def __init__(self, a=1, b=1, n=100, p=0.5, params=1000):
        self.a = a
        self.b = b
        self.n = n
        self.p = p
        self.x = np.linspace(0, 1, params)
        self.update()

    def update(self):
        """
        Update model from initial input or after modifying an attribute of the class
        """
        a = self.a
        b = self.b
        n = self.n
        p = self.p
        x = self.x
        k = p * n
        like_a = k + 1
        like_b = n - k + 1
        post_a = a + k
        post_b = b + n - k
        self.like_df = st.beta.pdf(x=x, a=like_a, b=like_b)
        self.prior_df = st.beta.pdf(x=x, a=a, b=b)
        self.post_df = st.beta.pdf(x=x, a=post_a, b=post_b)
        log_like = st.binom.logpmf(k=k, n=n, p=p)
        log_prior = st.beta.logpdf(x=p, a=a, b=b)
        log_post = st.beta.logpdf(x=p, a=post_a, b=post_b)
        log_marg = log_like + log_prior - log_post
        self.like = np.exp(log_like)
        self.prior = np.exp(log_prior)
        self.post = np.exp(log_post)
        self.marginal = np.exp(log_marg)

def get_models(shape_params, n=100, p=0.5, params=1000):
    """Compute multiple models

    Args:
        shape_params: List of tuples containing alpha and beta shape parameters. Example: [(a1, b1), (a2, b2), (a3, b3)]
        a: alpha parameter for beta prior distribution, defaults to 1
        b: beta parameter for beta prior distribution, defaults to 1
        n: sample size of simulated, defaults to 100
        p: proportion of successes, defaults to 0.5
        params: number of parameters to draw from probability density functions

    Returns:
        List of BetaBinomial class instances

    """
    models = []
    for i, param in enumerate(shape_params, start=1):
        m = BetaBinomial(a=param[0], b=param[1], n=100, p=0.5, params=1000)
        m.name = '{}'.format(i)
        models.append(m)
    return(models)
