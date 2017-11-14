import numpy as np
import scipy.stats as st

class BetaBinomial(object):
    def __init__(
        self,
        a=1,
        b=1,
        n=100,
        p=0.5,
        params=1000
    ):
        self.a = a
        self.b = b
        self.n = n
        self.p = p
        self.x = np.linspace(0, 1, params)
        self.update()

    def update(self):
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

def get_models(shape_params):
    models = []
    for i, param in enumerate(shape_params, start=1):
        m = BetaBinomial(a=param[0], b=param[1])
        m.name = '{}'.format(i)
        models.append(m)
    return(models)
